# SYS-002 — Idle RPG

Projet personnel de RPG mobile idle/AFK original, solo et hors ligne, conçu pour Android avec Unity 6 et C#.

Le dépôt sépare la spécification de conception, les décisions normatives et l'implémentation future. L'univers, les assets, les interfaces et le code du projet doivent rester originaux.

## État du projet

| Domaine | État |
|---|---|
| Spécification fonctionnelle | En cours de consolidation documentaire |
| Référentiel canonique | [GDD SYS-002 v1.1.1](docs/GDD/SYS-002_REFERENTIEL_V1.1.1/README.md) |
| Implémentation Unity | `not_started` |
| Tests d'exécution | `not_executed` |
| Branche principale | `main` |

Aucune validation documentaire ne constitue une preuve d'implémentation ou d'exécution de tests.

## Documentation

- [Référentiel GDD SYS-002 v1.1.1](docs/GDD/SYS-002_REFERENTIEL_V1.1.1/README.md)
- [GDD canonique intégral](docs/GDD/SYS-002_REFERENTIEL_V1.1.1/GDD_CANONIQUE_INTEGRAL.md)
- [Contrôle qualité et couverture](docs/GDD/SYS-002_REFERENTIEL_V1.1.1/CONTROLE_QUALITE_ET_COUVERTURE.md)
- [Statuts, restrictions et éléments en attente](docs/GDD/SYS-002_REFERENTIEL_V1.1.1/STATUTS_ET_RESTRICTIONS.md)
- [Méthode de maintenance documentaire](docs/GDD/SYS-002_REFERENTIEL_V1.1.1/CONTRIBUTION_ET_MAINTENANCE.md)

## Périmètre documentaire v1.1.1

- 14 chapitres structurés et reliés à l'historique source.
- 102 contrats explicitement ratifiés du Shared Combat Engine : `CORE`, `LIFE`, `SCHED`, `DMG`, `MOD` et `PAL`.
- 136 interventions décisionnelles suivies : 112 validations explicites, 20 prescriptions/corrections et 4 confirmations contextuelles, ces dernières conservant un niveau de preuve distinct.
- 20 contrats `CLF-001` à `CLF-020` encore `pending_validation`.
- `SYS-002.D.13.8` encore `not_started`.

La v1.1.1 corrige les métadonnées et l'hygiène de l'archive par rapport à la v1.1.0 ; elle n'ajoute aucune décision de conception. Le rapport de contrôle vérifie la traçabilité et l'intégrité structurelle, pas la validité mathématique indépendante de chaque formule.

## Structure prévue

```text
.
├── docs/GDD/SYS-002_REFERENTIEL_V1.1.1/
├── unity/                 # Projet Unity à ajouter lors de l'implémentation
├── README.md
└── .gitignore
```

## Règles de versionnement

- Le Markdown est le format source des spécifications.
- Les versions publiées du GDD sont immuables ; toute décision approuvée produit une nouvelle version.
- Les décisions non approuvées, les calibrations en attente et les statuts d'implémentation restent explicitement identifiés.
- Les corrections supplantent les règles antérieures sans effacer leur trace historique.
- Chaque publication doit passer le contrôle `python outils/gdd.py verify` dans le dossier du référentiel.
