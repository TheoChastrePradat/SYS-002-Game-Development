# Chapitre 00 — Vision, objectifs et conventions

**Autorité :** décisions expressément approuvées dans la conversation source. Les modèles obsolètes sont remplacés par les rectifications ultérieures ; les paramètres provisoires restent provisoires.

**Statut du chapitre :** `functionally_specified` pour ses spécifications validées ; aucune exécution de test ou implémentation ne découle de ce statut.

**Traçabilité :** 2 décision(s) du propriétaire. Toutes les références `Txxx` renvoient à `references/HISTORIQUE_SOURCE_ORIGINAL.md`.

## Décisions structurantes en vigueur

| Sujet | Règle approuvée | Justificatif |
|---|---|---|
| Produit | RPG mobile idle/AFK original, solo, automatique, sans monétisation | T002, T005 |
| Plateforme | Android, application locale indépendante | T076–T078 |
| Moteur et langage | **Unity 6 / C#**, remplaçant Godot / GDScript envisagés au départ | T076–T078 |
| Architecture | Simulation déterministe, indépendance du rendu, séparation domaine/application/infrastructure/présentation | T005, T074, T078 |
| Données | Configurations versionnées, persistance SQLite locale, architecture extensible | T076, T111 |
| Administration | Outils développeur privés contrôlant la progression et les ressources, par services métier | T002, T005 |

Le jeu doit utiliser des assets, un univers, des interfaces et un code originaux. Les mécanismes généraux constituent l'inspiration, pas un transfert d'actifs propriétaires.


## Registre détaillé des décisions approuvées


### T002 · T002 · 17/11/2026 16:36:22

**Nature :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Ligne d’approbation source :** 23 · **Ligne de formalisation :** 30.

**Décision / prescription originale (texte intégral du propriétaire) :**

Le sujet de cette instance conversationnelle portera sur un nouveau projet.
Tu connais certainement le jeu mobile Legend of Mushrooms.
Je souhaiterais le reproduire pour avoir ma propre version. Dans la mesure à ne pas créer de plagia il faudrait peut être modifier certaines choses, mais globalement je souhaite reproduire ce jeu personnellement afin de pouvoir jouer en bénéficiant de tous les avantages en jeu.


**Source technique :** réponse consécutive et proposition précédant cette validation, consultables dans l’historique original. Aucun extrait automatique n’a été retenu faute de délimitation non ambiguë.


### T005 · T005 · 17/11/2026 16:56:52

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 1035 · **Ligne de formalisation :** 1040.

**Décision / prescription originale (texte intégral du propriétaire) :**

Décision GDD SYS-002 : modèle de combat A. Précisions : Les déplacements, attaques et compétences sont automatiques. Le joueur observe le combat et intervient principalement dans la progression.. Poursuivons la spécification du moteur de combat.


**Source technique :** réponse consécutive et proposition précédant cette validation, consultables dans l’historique original. Aucun extrait automatique n’a été retenu faute de délimitation non ambiguë.

