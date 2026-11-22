# GDD SYS-002 — Référentiel canonique versionné

**Version documentaire :** 1.1.1 (22 novembre 2026)  
**Produit :** Idle RPG original, solo / offline, Android, Unity 6 / C#  
**Source :** export original de la conversation « Activation du mode absolu » (150 échanges)  
**Empreinte SHA-256 source :** `9ff27efc833dcadeabba8db617d5ebdf7000b28c55904a73e7723f2ee034b1d2`  
**Statut du corpus :** décisions de conception approuvées. `implementation=not_started`, `tests=not_executed` pour les sous-systèmes où ces statuts ont été explicitement consignés.  
**Point de reprise :** `SYS-002.D.13.7.12.1`, 20 contrats `CLF` proposés, encore non ratifiés.

## Préambule

Ce référentiel constitue la **source de vérité documentaire**, pas une preuve d'implémentation. Les décisions obsolètes sont identifiées comme telles dans le registre des restrictions. Les contenus de validation demeurent intégralement traçables à leurs tours d'origine.

**Les extraits techniques intégrés aux décisions ne peuvent pas introduire de règle supplémentaire non couverte par la validation.** Un schéma représente un mécanisme admis ; s'il entre en conflit avec une correction ultérieure, la correction prévaut. Les dossiers techniques détaillés D.13.1 à D.13.6 sont des pièces d'appui approuvées avec les contrats correspondants.

## Table des matières

- [Chapitre 00 — Vision, objectifs et conventions](chapitres/00_vision_objectifs_et_conventions.md)
- [Chapitre 01 — Modèle mathématique — dégâts bruts](chapitres/01_modele_mathematique_degats_bruts.md)
- [Chapitre 02 — Défense, pénétration et résistances](chapitres/02_defense_penetration_et_resistances.md)
- [Chapitre 03 — Critiques et dégâts critiques](chapitres/03_critiques_et_degats_critiques.md)
- [Chapitre 04 — Évasion et probabilités de toucher](chapitres/04_evasion_et_probabilites_de_toucher.md)
- [Chapitre 05 — Cadence, vitesse et temps](chapitres/05_cadence_vitesse_et_temps.md)
- [Chapitre 06 — Modificateurs, groupes et priorités](chapitres/06_modificateurs_groupes_et_priorites.md)
- [Chapitre 07 — Dictionnaire des caractéristiques](chapitres/07_dictionnaire_des_caracteristiques.md)
- [Chapitre 08 — Combo, contre-attaque, contrôle, blocage et soins](chapitres/08_combo_contre_attaque_controle_blocage_et_soins.md)
- [Chapitre 09 — Acolytes — modèle et combat](chapitres/09_acolytes_modele_et_combat.md)
- [Chapitre 10 — Acolytes — progression, invocations et persistance](chapitres/10_acolytes_progression_invocations_et_persistance.md)
- [Chapitre 11 — Équipement et Lampe Magique](chapitres/11_equipement_et_lampe_magique.md)
- [Chapitre 12 — Classes, spécialisations, compétences et Éveils](chapitres/12_classes_specialisations_competences_et_eveils.md)
- [Chapitre 13 — Shared Combat Engine — contrats transversaux](chapitres/13_shared_combat_engine_contrats_transversaux.md)
- [Contrôle de qualité et couverture](CONTROLE_QUALITE_ET_COUVERTURE.md)
- [Statuts, restrictions et points non validés](STATUTS_ET_RESTRICTIONS.md)
- [Méthode de validation et de sauvegarde](CONTRIBUTION_ET_MAINTENANCE.md)
- [Contrats et dossiers techniques du moteur partagé](annexes/SPECIFICATIONS_DETAILLEES_D13.1_A_D13.6.md)

## Portée

Le GDD est découpé en quatorze chapitres, contient le **texte intégral de chaque prescription propriétaire enregistrée**, et inclut les 102 contrats ratifiés `CORE`/`LIFE`/`SCHED`/`DMG`/`MOD`/`PAL` avec leurs descriptions et dossiers techniques. Les formules et schémas présents dans les dossiers techniques validés demeurent sous leur forme originelle. Les sources historiques complètes et les fichiers CSV sont disponibles dans `references/`.

Le référentiel doit évoluer par **versions immuables**, avec génération d'archive immédiatement après chaque approbation. Aucun accès persistant à un dépôt Git externe n'est implicite.
