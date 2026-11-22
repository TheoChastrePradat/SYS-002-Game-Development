#!/usr/bin/env python3
"""SYS-002 normative GDD ledger: verify, accept approved changes, build and snapshot.

No inference or autonomous approval. The owner-supplied validated payload is the single
mutable surface; current reference files and historical decisions are append-only.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import re
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
MANIFEST = BASE / 'MANIFEST_SHA256.json'
APPROVALS = BASE / 'references' / 'APPROBATIONS_ORIGINE.csv'
CONTRACTS = BASE / 'references' / 'CONTRATS_RATIFIES.csv'
SRC = BASE / 'references' / 'HISTORIQUE_SOURCE_ORIGINAL.md'
SRC_SHA = '9ff27efc833dcadeabba8db617d5ebdf7000b28c55904a73e7723f2ee034b1d2'
APPROVED_PREFIX = ('CORE-', 'LIFE-', 'SCHED-', 'DMG-', 'MOD-', 'PAL-', 'CLF-')

def fail(s: str) -> None:
    raise SystemExit('ERREUR: ' + s)

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def rel(path: Path) -> str:
    return path.relative_to(BASE).as_posix()

def files_for_manifest() -> list[Path]:
    return [p for p in sorted(BASE.rglob('*')) if p.is_file() and p != MANIFEST and 'releases' not in p.relative_to(BASE).parts and p.name != '.DS_Store' and '__pycache__' not in p.relative_to(BASE).parts and p.suffix != '.pyc']

def build_manifest() -> dict:
    return {
        'format': 'sys002-gdd-sha256-v1',
        'source_sha256': SRC_SHA,
        'generated_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'files': [{'path': rel(p), 'sha256': digest(p), 'bytes': p.stat().st_size} for p in files_for_manifest()],
    }

def write_manifest() -> None:
    MANIFEST.write_text(json.dumps(build_manifest(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def read_csv(path: Path) -> list[dict]:
    with path.open(newline='', encoding='utf-8-sig') as f:return list(csv.DictReader(f))

def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)

def verify() -> dict:
    if not SRC.is_file() or digest(SRC) != SRC_SHA: fail('la source historique a été modifiée')
    required=['README.md','GDD_CANONIQUE_INTEGRAL.md','STATUTS_ET_RESTRICTIONS.md','ARCHITECTURE_ET_CARTOGRAPHIE.md','CONTRIBUTION_ET_MAINTENANCE.md']
    for fn in required:
        if not (BASE/fn).is_file(): fail('document requis absent: '+fn)
    chapters=sorted((BASE/'chapitres').glob('*.md'))
    codes=[int(p.name[:2]) for p in chapters if re.match(r'^\d\d_',p.name)]
    if len(codes)!=len(chapters) or len(codes)<14 or set(codes)!=set(range(max(codes)+1)) or len(codes)!=len(set(codes)):
        fail('numérotation des chapitres incomplète ou dupliquée')
    original=read_csv(APPROVALS)
    if len(original)!=136 or len({x['turn'] for x in original})!=136:fail('le registre historique des 136 approbations est incomplet')
    csv_contracts=read_csv(CONTRACTS)
    ids=[x['id'] for x in csv_contracts]
    if len(ids)!=len(set(ids)) or len(ids)<102:fail('contrats ratifiés en doublon ou incomplets')
    expected={f'{pre}-{i:03d}' for pre,count in [('CORE',12),('LIFE',16),('SCHED',18),('DMG',24),('MOD',24),('PAL',8)] for i in range(1,count+1)}
    if not expected.issubset(ids):fail('les 102 contrats originaux ne sont pas tous présents')
    archive=(BASE/'annexes'/'SPECIFICATIONS_DETAILLEES_D13.1_A_D13.6.md')
    if not archive.exists():fail('annexe de spécifications ratifiées manquante')
    if not MANIFEST.is_file():fail('aucun manifest SHA-256 (utiliser seal seulement après modification autorisée)')
    m=json.loads(MANIFEST.read_text('utf-8'))
    if m.get('source_sha256')!=SRC_SHA:fail('empreinte de provenance différente')
    actual={rel(p): digest(p) for p in files_for_manifest()}
    expected_hashes={x['path']:x['sha256'] for x in m.get('files',[])}
    if actual!=expected_hashes:
        problems=[p for p in sorted(set(actual)|set(expected_hashes)) if actual.get(p)!=expected_hashes.get(p)]
        fail('dérive entre le manifeste et les fichiers: '+', '.join(problems[:12]))
    # CLF are allowed only if their own owner-authorized decision is attached.
    if any(x.startswith('CLF-') for x in ids):
        proof_files=list((BASE/'decisions').glob('SYS-002.D.13.7*.md'))
        if not proof_files:fail('contrats CLF présents sans preuve de validation dans decisions/')
        proof='\n'.join(p.read_text('utf-8') for p in proof_files)
        if not all(x in proof for x in [f'CLF-{i:03d}' for i in range(1,21)]):
            fail('dossier de décision CLF incomplet')
    # no tacit implementation claims across status register
    if not (BASE/'STATUTS_ET_RESTRICTIONS.md').read_text('utf-8').find('pending_validation')>=0:
        fail('les points de validation en attente ne sont pas tracés')
    return {'result':'OK', 'historical_approvals':len(original), 'ratified_contracts':len(ids), 'chapters':len(chapters), 'supplementary_decisions':len(list((BASE/'decisions').glob('*.md'))), 'files_verified':len(actual), 'source_sha256':SRC_SHA}

def latest_files() -> list[Path]:
    return sorted((BASE/'chapitres').glob('*.md'))

def rebuild_integral():
    head=(BASE/'README.md').read_text('utf-8')
    chunks=[head]
    for p in latest_files():chunks.append('\n---\n\n'+p.read_text('utf-8'))
    chunks.append('\n---\n\n'+(BASE/'annexes'/'SPECIFICATIONS_DETAILLEES_D13.1_A_D13.6.md').read_text('utf-8'))
    chunks.append('\n---\n\n'+(BASE/'STATUTS_ET_RESTRICTIONS.md').read_text('utf-8'))
    (BASE/'GDD_CANONIQUE_INTEGRAL.md').write_text('\n'.join(chunks)+'\n',encoding='utf-8')

def cmd_add(a):
    ident=a.id.strip()
    if not re.fullmatch(r'SYS-\d{3}(?:\.\w+)+', ident):fail('identifiant invalide')
    if not re.fullmatch(r'T\d{3,}',a.decision_source):fail('référence d’approbation invalide (Txxx)')
    if not (a.approved and a.approval_text.strip()):fail('le texte d’approbation propriétaire et --approved sont obligatoires')
    if not re.search(r'(?i)(je valide|valid(?:ation|é|ée|ons)|approuv|je choisis|modèle\s+[ABC])',a.approval_text):fail('aucune validation explicite identifiable; enregistrer une décision vérifiable')
    inp=Path(a.text_file)
    if not inp.is_file():fail('fichier d’entrée introuvable')
    body=inp.read_text('utf-8').strip()
    if len(body)<30:fail('spécification vide ou trop courte')
    if not re.fullmatch(r'\d{2}',a.chapter):fail('chapitre invalide: deux chiffres attendus')
    if any(ident==x['id'] for x in read_csv(CONTRACTS)) or (BASE/'decisions'/f'{ident}.md').exists():fail('un identifiant ne peut jamais écraser une décision déjà ratifiée')
    chapters=[p for p in latest_files() if p.name.startswith(a.chapter+'_')]
    next_ch=f'{max(int(p.name[:2]) for p in latest_files())+1:02d}'
    is_new=(len(chapters)==0 and a.chapter==next_ch)
    if len(chapters)!=1 and not is_new:fail('chapitre cible inconnu ou ambigu (nouveau chapitre doit être séquentiel)')
    if is_new and (not a.chapter_title or len(a.chapter_title.strip())<4):fail('un nouveau chapitre requiert --chapter-title')
    if MANIFEST.is_file():verify()
    if is_new:
        title=a.chapter_title.strip()
        chpath=BASE/'chapitres'/f'{a.chapter}_{re.sub(r"[^a-z0-9]+","_",title.lower()).strip("_")}.md'
        chpath.write_text(f'# Chapitre {a.chapter} — {title}\n\n**Statut :** en cours de spécification, uniquement les décisions ratifiées sont intégrées.\n',encoding='utf-8')
        chapters=[chpath]
        readme=BASE/'README.md'
        rs=readme.read_text('utf-8')
        toc=f'- [Chapitre {a.chapter} — {title}](chapitres/{chpath.name})\n'
        rs=rs.replace('- [Statuts, restrictions et points non validés]',toc+'- [Statuts, restrictions et points non validés]')
        readme.write_text(rs,encoding='utf-8')
    proof=f'''# {ident} — Décision documentaire ratifiée\n\n**Propriétaire :** validation explicite (source `{a.decision_source}`)  \n**Statut :** `functionally_specified` · implémentation `not_started` · tests `not_executed`  \n**Approbation exacte :** {a.approval_text.strip()}\n\n## Texte normatif approuvé\n\n{body}\n'''
    contract_rows=[]
    if ident.startswith('SYS-002.D.13.7'):
        found=set(re.findall(r'\bCLF-\d{3}\b',body))
        expected={f'CLF-{i:03d}' for i in range(1,21)}
        if found!=expected:fail('la validation D13.7 doit fournir le texte complet des 20 contrats CLF-001 à CLF-020')
        # A plain 'Je valide' is admissible only because the full 20-contract list is
        # present, the explicit prior proposal is bound to the source turn, and
        # the owner confirms the whole pending item in this tracked workflow.
        for no in range(1,21):
            k=f'CLF-{no:03d}'
            row=next((x for x in body.splitlines() if re.search(r'\b'+re.escape(k)+r'\b',x)),None)
            if not row:fail('contrat sans ligne descriptive: '+k)
            parts=[x.strip().strip('`') for x in row.strip().strip('|').split('|')]
            statement=' | '.join(p for p in parts if k not in p).strip()
            if len(statement)<8:fail('contrat sans clause exploitable: '+k)
            contract_rows.append(dict(id=k,statement=statement,module='SYS-002.D.13.7',name='Combat Lifecycle & Finalization',approved_turn=a.decision_source,proposal_turn='source-historique',decision=ident))
    (BASE/'decisions'/f'{ident}.md').write_text(proof,encoding='utf-8')
    with chapters[0].open('a',encoding='utf-8') as f:f.write('\n---\n\n'+proof+'\n')
    if contract_rows:
        all_rows=read_csv(CONTRACTS);all_rows.extend(contract_rows)
        write_csv(CONTRACTS,all_rows,list(all_rows[0]))
        statuses=BASE/'STATUTS_ET_RESTRICTIONS.md'
        s=statuses.read_text('utf-8')
        s=s.replace('`SYS-002.D.13.7.12.1`: `CLF-001` à `CLF-020` = `pending_validation`. **Aucun de ces contrats n\'est ratifié dans la version 1.1.**',f'`SYS-002.D.13.7.12.1`: `CLF-001` à `CLF-020` = `functionally_specified`, ratifiés sous `{a.decision_source}`. Implémentation et tests toujours non effectués.')
        statuses.write_text(s,encoding='utf-8')
    with (BASE/'CHANGELOG.md').open('a',encoding='utf-8') as f:f.write(f'- {datetime.now(timezone.utc).isoformat(timespec="seconds")}: `{ident}` ratifié par `{a.decision_source}`, ajouté au chapitre {a.chapter}.\n')
    rebuild_integral()
    write_manifest()
    print(json.dumps(verify(),ensure_ascii=False,indent=2))

def cmd_snapshot(a):
    info=verify()
    if not re.fullmatch(r'\d+\.\d+\.\d+',a.version):fail('version invalide: attendu X.Y.Z')
    out=BASE.parent/f'GDD_SYS-002_REFERENTIEL_V{a.version}.zip'
    if out.exists():fail('archive versionnée déjà existante, écrasement interdit: '+out.as_posix())
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=7) as z:
        for p in sorted(BASE.rglob('*')):
            if p.is_file() and 'releases' not in p.relative_to(BASE).parts and '__pycache__' not in p.relative_to(BASE).parts and p.suffix != '.pyc':
                z.write(p,arcname=BASE.name+'/'+rel(p))
    print(json.dumps({'archive':str(out),'size_bytes':out.stat().st_size,'sha256':digest(out),**info},ensure_ascii=False,indent=2))

def cli():
    p=argparse.ArgumentParser(description='GDD SYS-002 — gestion locale versionnée')
    sub=p.add_subparsers(dest='cmd',required=True)
    sub.add_parser('verify',help='Vérifie empreintes, contrats, chapitres, provenance')
    sub.add_parser('seal',help='Recalcule le manifeste après une modification délibérée ; usage éditorial contrôlé')
    sub.add_parser('build',help='Regénère le GDD intégral depuis les chapitres')
    s=sub.add_parser('snapshot',help='Crée une archive immuable de la version')
    s.add_argument('--version',required=True)
    s=sub.add_parser('add',help='Ajoute une décision ratifiée sans écraser les précédentes')
    s.add_argument('--id',required=True);s.add_argument('--chapter',required=True);s.add_argument('--chapter-title',required=False)
    s.add_argument('--decision-source',required=True);s.add_argument('--approval-text',required=True)
    s.add_argument('--text-file',required=True);s.add_argument('--approved',action='store_true')
    a=p.parse_args()
    if a.cmd=='verify':print(json.dumps(verify(),ensure_ascii=False,indent=2))
    elif a.cmd=='seal':write_manifest();print('MANIFEST_SHA256.json renouvelé après modification délibérée.')
    elif a.cmd=='build':rebuild_integral();write_manifest();print(json.dumps(verify(),ensure_ascii=False,indent=2))
    elif a.cmd=='add':cmd_add(a)
    elif a.cmd=='snapshot':cmd_snapshot(a)
if __name__=='__main__':cli()
