# Statuts, restrictions et périmètre non encore ratifié

## Sémantique des états

- `proposed` : proposition écrite sans approbation.
- `pending_validation` : ensemble de contrats soumis, non encore accepté.
- `functionally_specified` : comportement normé dans le GDD, pas de code livré.
- `calibration_pending` : valeur ou comportement chiffré à confirmer.
- `provisional` : profil accepté comme hypothèse temporaire ; il ne s'agit pas d'une mesure confirmée.
- `not_started` : implémentation non commencée.
- `not_executed` : aucun résultat de test enregistré.
- `implemented` et `verified` : **réservés aux preuves ultérieures**, jamais inférés d'une validation documentaire.

## Historique des rectifications qui font autorité

| Ancienne formulation | Référence originale | Règle active | Source |
|---|---|---|---|
| Godot / GDScript | Début du projet | Unity 6 / C# | T076–T078 |
| Évasion portée `inherit` | T013 | Portée `expanded`, plafonds PvE 100 %, PvP 80 % | T014 |
| Croissance acolytes convexes / exponentielles | T049–T050 | Croissance linéaire constante | T051–T052 |
| Fusion candidats = `all_catalog_entries` | T064 | Carte débloquée par tirage préalablement | T065 |

## Périmètre non validé

- `SYS-002.D.13.7.12.1`: `CLF-001` à `CLF-020` = `pending_validation`. **Aucun de ces contrats n'est ratifié dans la version 1.1.1.**
- `SYS-002.D.13.8`: `not_started`.
- Les données des catalogues et coefficients dont la source mentionne `catalog_pending`, `calibration_pending`, `defense_calibration_pending`, `damage_mode_calibration_pending` ou `unknown` restent ouvertes.
- Les résultats d'exécution de tests et l'implémentation Unity ne sont pas inférés du GDD.

La conversation originale est une **preuve historique**, non une seconde source normative active. Le document canonique est constitué des chapitres, des clauses contractuelles approuvées, et des rectifications datées.
