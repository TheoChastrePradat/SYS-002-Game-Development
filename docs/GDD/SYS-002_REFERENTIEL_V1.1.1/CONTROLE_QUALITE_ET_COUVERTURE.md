# Contrôle de couverture documentaire — v1.1.1

**Date :** 22 novembre 2026. **Nature du contrôle :** intégrité textuelle, traçabilité et cohérence structurelle ; aucune vérification d'exécution du jeu.

## Couverture

| Mesure | Valeur | Méthode |
|---|---:|---|
| Messages du propriétaire dans la source exportée | 150 | Reconstruction `T001`–`T150` |
| Interventions retenues au registre | 136 | Décisions, confirmations ou prescriptions |
| Validations explicitement formulées | 112 | Registre propriétaire |
| Prescriptions / corrections directes | 20 | Registre propriétaire |
| Confirmations contextuelles | 4 | Registre distinct, niveau de preuve inférieur |
| Chapitres | 14 | `chapitres/` |
| Contrats explicitement ratifiés | 102 | `references/CONTRATS_RATIFIES.csv` |
| Sections d'explication technique délimitées et rapprochées d'une validation | 120 | Extraction conservatrice par identifiant |
| Schémas Mermaid dans les formalismes rapprochés des décisions | 31 | Comptage des blocs Mermaid |
| Schémas Mermaid dans les six dossiers techniques ratifiés D.13.1–D.13.6 | 13 | Comptage des blocs Mermaid |
| Équations blocs `$$...$$` dans les chapitres | 305 | Comptage des blocs affichés |
| Équations blocs `$$...$$` dans les annexes ratifiées | 58 | Comptage des blocs affichés |

## Précautions d'interprétation

1. Ce comptage montre que les informations de conception, les schémas et les équations **rattachables de manière traçable** ont été transférés ; il ne prouve pas une relecture mathématique indépendante de chaque formule.
2. Les extraits de formalisation ont été limités par identifiant pour éviter d'incorporer automatiquement la proposition de la section suivante ; **une lecture de contrôle par chapitre reste nécessaire** pour statuer sur les ambiguïtés héritées.
3. Les anciennes formulations explicitement supplantées (croissance des acolytes, fusion, portée de l'évasion, changement de moteur) sont conservées comme preuve historique, non comme règle actuelle.
4. Les décisions contextuelles (`Oui`, `Parfait`) sont conservées avec leur niveau de preuve propre, distinct des validations explicites. Le rattachement à une proposition doit pouvoir être réexaminé.
5. Les contrats `CLF-001` à `CLF-020` restent `pending_validation`, et D.13.8 n'a pas été commencé. Les valeurs `unknown`, `provisional` et `calibration_pending` ne sont pas traitées comme des faits calibrés.
6. Le document contient des liens vers les sources historiques. Les liens vers des références externes mentionnées dans le dialogue **n'ont pas été revérifiés** dans cette construction et ne sont pas des preuves nouvelles.

## Vérifications techniques du système d'archivage

- `verify` : empreinte SHA-256 du texte original, 102 contrats minimums, 14 chapitres minimums, unicité d'identifiants et contrôle de chaque fichier via le manifeste.
- `add` : création d'une nouvelle décision datée sans écraser un ID existant, incorporation à son chapitre, reconstruction du GDD intégral et mise à jour du manifeste.
- `snapshot` : fichier ZIP versionné avec protection contre l'écrasement d'une version antérieure.
- Contrôle négatif : modification artificielle d'un chapitre dans une copie du référentiel, correctement refusée par `verify`.
- Contrôle positif : ajout fictif d'un nouveau chapitre 14 dans une **copie temporaire**, suivi d'une vérification réussie. Aucun contrat fictif n'est conservé dans l'archive livrée.

## Prochaine opération documentaire

Révision contradictoire du GDD chapitre par chapitre pour vérifier les 136 rattachements et les équations. Le référentiel produit est **une reconstruction versionnée**, et non un acte de validation globale supplémentaire fourni par le propriétaire.
