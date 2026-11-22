# Contrat documentaire et méthode de maintenance

## Définition du corpus normatif

Le GDD a pour source première l'historique ChatGPT exporté le 21 novembre 2026. **Les approbations du propriétaire constituent l'autorité finale.** Les 136 interventions conservées dans les registres comprennent validations explicites, approbations contextuelles et prescriptions/corrections directes. Les approbations contextuelles restent identifiées comme telles, non confondues avec une validation littérale d'un identifiant.

Chaque chapitre comprend : son identifiant stable, le texte approuvé dans sa forme complète, les choix normatifs, sa source `Txxx`, et les formalismes techniques récupérables sans mélange avec les propositions suivantes. Les 102 contrats explicitement ratifiés du Shared Combat Engine sont repris **mot pour mot**, complétés par les dossiers détaillés contenant schémas, formules, invariants et tests.

## Hiérarchie des règles

1. Correction explicite postérieure du propriétaire.
2. Décision d'approbation explicite avec ID et valeurs.
3. Approbation contextuelle de la proposition immédiatement précédente, uniquement quand le sujet est identifiable.
4. Description technique correspondant à une règle acceptée (explicative, non source autonome de nouvelles décisions).
5. Historique source (pour vérification et résolution des écarts).

Si une même section comporte des versions concurrentes, **ne pas fusionner les formules par intuition** ; relever l'incompatibilité dans `STATUTS_ET_RESTRICTIONS.md` et solliciter une nouvelle validation.

## Granularité des changements

Une unité de modification = une nouvelle décision formellement ratifiée, avec identifiant unique, texte complet, section cible, références source et statut d'implémentation. Les corrections ne réécrivent jamais l'historique : elles le **supplantent** avec un lien bidirectionnel (`supersedes`, `superseded_by`).

## Procédure après chaque approbation

1. Consigner le nouvel identifiant, le texte exact de la décision et sa source.
2. Reporter les clauses approuvées, diagrammes Mermaid, équations LaTeX, tables de données, invariants et tests à leur section.
3. Mettre en évidence `provisional`, `unknown` et calibrations en attente.
4. Vérifier qu'aucune ancienne règle n'est redevenue active.
5. Exécuter `python outils/gdd.py verify` pour vérifier l'intégrité et les invariants du référentiel.
6. Exécuter `python outils/gdd.py snapshot --version X.Y.Z` ; sauvegarder l'archive et conserver une copie Git.
7. Remettre au propriétaire le nouveau fichier ZIP et le document consolidé. Aucun enregistrement automatique dans un dossier distant n'est supposé.

## Exemples d'utilisation

Dans le dossier racine du référentiel :

```bash
python outils/gdd.py verify
python outils/gdd.py add --id SYS-002.D.13.7.12.1 --chapter 13 --decision-source T151 --approval-text "Je valide les contrats CLF-001 à CLF-020" --text-file /chemin/contrats_valides.md --approved
python outils/gdd.py verify
python outils/gdd.py snapshot --version 1.2.0
```

Le deuxième exemple ne doit être exécuté **qu'après validation explicite** et avec l'intégralité des contrats ratifiés dans le fichier source ; l'utilitaire refuse un ID déjà présent.

## Conventions des documents

- Markdown UTF-8 est la source ; Mermaid ` ```mermaid ` pour les architectures, LaTeX `\[ ... \]` ou `$$...$$` pour les formules.
- IDs `SYS-*`, `Txxx`, contrats de domaine et versions `vX.Y.Z` restent stables.
- Les noms et identifiants de classes, d'événements et de données doivent rester strictement identiques à leurs décisions ratifiées.
- N'écrire **jamais** `tested`, `verified` ou `implemented` sans preuves de build ou de tests.
- Une nouvelle validation **modifie le GDD dans le tour où elle est traitée**, puis produit un artefact à télécharger. Cela ne constitue pas une sauvegarde automatique en arrière-plan.
