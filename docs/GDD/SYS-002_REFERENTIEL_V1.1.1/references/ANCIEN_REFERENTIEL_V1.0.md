# GDD — SYS-002 · Référentiel normatif des décisions approuvées

**Version documentaire :** 1.0 · 21 novembre 2026  
**Objet :** Idle RPG original inspiré de mécaniques générales, en développement personnel.  
**Source immuable :** `ChatGPT-Activation du mode absolu-20261121-2332.md` (150 interventions utilisateur / 150 réponses), SHA-256 `9ff27efc833dcadeabba8db617d5ebdf7000b28c55904a73e7723f2ee034b1d2`.  
**Statut :** référentiel **approuvé documentairement**, **non implémenté**.  
**Point d'arrêt :** `SYS-002.D.13.7.12.1` — projet de contrats `CLF-001..CLF-020` **non approuvé**, donc **absent du présent référentiel**.

## 0. Convention normative et traçabilité

Ce document contient **uniquement** les choix expressément approuvés par le propriétaire, ses corrections de spécification, et les contrats dont l'ensemble a reçu un acte explicite de validation. Il exclut les variantes purement proposées, les questions de validation, les choix abandonnés et les 20 contrats CLF en attente. Quand un profil a été approuvé comme *provisoire*, c'est le **statut provisoire** qui est approuvé : ses chiffres ne sont pas des mesures confirmées.

**Autorité documentaire :** un choix explicite de l'utilisateur prévaut sur une proposition de l'assistant ; une correction postérieure prévaut sur un choix ancien pour la même règle ; les inconnues gardent la valeur `unknown` ou `*_pending` enregistrée. Les libellés de contrat restent identiques à ceux ratifiés. `functionally_specified` n'implique ni code exécuté, ni test passé.

**Niveaux de preuve :** `APPROBATION_EXPLICITE` (validation ou modèle choisi par l'utilisateur) ; `APPROBATION_CONTEXTUELLE` (réponse d'accord rattachée à la proposition immédiatement précédente et confirmée dans la réponse suivante) ; `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` (règle directement transmise ou corrigée par le propriétaire). Chaque décision indique son tour `Txxx` et la ligne de son message source ; la reconstruction intégrale, le registre CSV et l'export brut sont conservés séparément.

> Note de lecture : les tableaux de formalisation cités sous chaque décision proviennent de la **réponse après accord**. Ce ne sont pas des propositions nouvelles reprises comme si elles avaient été approuvées. Lorsque le tableau est absent ou ambigu, seule l'approbation utilisateur est retranscrite.

## 1. Principes et architecture active

| Domaine | Règle en vigueur | Approbation(s) |
|:--|:--|:--|
| Périmètre | RPG mobile idle/AFK original, PvE automatique, solo/offline, sans monétisation, mode administrateur privé intégré | `T002 / T004 / T005` |
| Combat | Déplacements, attaques et compétences automatiques ; l’intervention du joueur porte essentiellement sur la préparation et la progression | `T005` |
| Architecture | Moteur de simulation déterministe, découplé du rendu, avec événements horodatés et RNG reproductible | `T005 / T145 / T147` |
| Technologie | Unity 6 + C# ; Android initialement, développement sur PC ; Godot/GDScript sont des hypothèses anciennes remplacées | `T076 / T077` |
| Persistance | SQLite locale, configurations JSON versionnées, exécution standalone_offline | `T076` |
| Organisation | Monolithe modulaire, ports/adapters, interfaces explicites, cinq assemblies communes par couche | `T074 / T078` |
| Mathématiques dégâts | Construction hybride : A × C × (1+B) × ∏Mᵢ ; groupes additifs et multiplicateurs indépendants | `T007` |
| Mitigation DEF | Rendement décroissant K/(DEF_eff+K), K configurable et à calibrer | `T008` |
| Évasion | Périmètre élargi validé pour notre jeu : normales, combos, contre-attaques, acolytes ; plafonds PvE 100 %, PvP 80 % ; taux affiché distinct du taux effectif | `T013 / T014` |
| Cadence | Attaques par seconde, première attaque immédiate à portée, modification de vitesse conservant la progression du cycle ; horloge en microsecondes | `T015 / T016` |
| Modificateurs | Groupes déclarés, bonus plats en premier, additifs au sein d’un groupe, indépendance des groupes multiplicatifs, rejets des conflits non déclarés | `T017 / T018 / T019` |
| Quantification | Dégâts minimum 0 et arrondi vers le bas à l’application finale selon la règle validée ; D.13.4 introduit un profil de quantification déterministe par composante | `T020 / T148` |
| Acolytes | Un seul niveau 1–200 par acolyte, distinct des compétences du personnage ; croissance linéaire à incrément constant, profil individuel réutilisable | `T043 / T051 / T052` |
| Fusion | Un résultat de fusion est éligible seulement si sa carte a déjà été débloquée par tirage ; cette correction remplace all_catalog_entries | `T065` |
| Portails d’invocation | Portails indépendants ; taux normalisés ; XP avant tirage, lots séquentiels, RNG injectable, réservation/débit durables et récupération après interruption | `T048 / T059 / T060 / T061 / T062 / T066 / T069` |
| Lampe magique | Niveau du joueur et niveau de lampe séparés ; génération d’équipement par rareté, emplacement, plages et affixes selon règles validées | `T080 / T081 / T094 / T095 / T096` |
| Classes | Quatre familles et leurs spécialisations décrites, contrats fonctionnels Guerrier, Archer, Mage et Spirit Channeler validés ; données/calibrations non achevées | `T124 / T131 / T137 / T143` |
| Combat partagé | 102 contrats approuvés répartis en CORE 12, LIFE 16, SCHED 18, DMG 24, MOD 24, PAL 8 | `T145–T150` |

### 1.1 Supersessions appliquées avant consolidation

| Domaine | Règle courante approuvée | Tour de référence |
|:--|:--|:--|
| Moteur | Unity 6 / C# remplace Godot / GDScript | `T076–T078` |
| Évasion | Portée `expanded` approuvée ultérieurement ; l'ancienne proposition `inherit` n'est plus normative | `T013–T014` |
| Croissance des acolytes | Linéaire à incrément constant ; les anciens profils convexes et exponentiels sont écartés | `T051–T052` |
| Fusion | Carte déjà débloquée par tirage obligatoire ; la règle `all_catalog_entries` est écartée | `T064–T065` |

---

## 2. Décisions par système — registre normatif

Les sous-sections suivantes consignent les **choix approuvés**, les **précisions expressément imposées**, les **statuts conservés** et les **tableaux de formalisation** validés. Aucun passage de discussion ouvert n'est transcrit comme décision.

### 00 - Vision, cadrage, architecture et modèle de combat

#### T002 · T002

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T002`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t002) — export ligne 23; réponse ligne 30.

**Prescription approuvée :** Le sujet de cette instance conversationnelle portera sur un nouveau projet.
Tu connais certainement le jeu mobile Legend of Mushrooms.
Je souhaiterais le reproduire pour avoir ma propre version. Dans la mesure à ne pas créer de plagia il faudrait peut être modifier certaines choses, mais globalement je souhaite reproduire ce jeu personnellement afin de pouvoir jouer en bénéficiant de tous les avantages en jeu


#### T005 · T005

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T005`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t005) — export ligne 1035; réponse ligne 1040.

**Prescription approuvée :** Décision GDD SYS-002 : modèle de combat A. Précisions : Les déplacements, attaques et compétences sont automatiques. Le joueur observe le combat et intervient principalement dans la progression.. Poursuivons la spécification du moteur de combat


### 01 - Construction des dégâts bruts

#### T006 · SYS-002.D.1

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T006`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t006) — export ligne 1509; réponse ligne 1515.

**Prescription approuvée :** Continuons.
Pour chaque étape, donnes moi la possibilité de valider les choix afin d'apporter une modification/spécification si necessaire

**Tableau de formalisation consécutive à la validation :**

| ID | Spécification | Statut |
|--------|--------|--------|
| D.1 | Construction des dégâts bruts | (En cours) |
| D.2 | Mitigation par la défense | À définir |
| D.3 | Coups critiques | À définir |
| D.4 | Précision et esquive | À définir |
| D.5 | Vitesse d'attaque | À définir |
| D.6 | Multiplicateurs et cumul des bonus | À définir |
| D.7 | Ordre d'application des effets | À définir |
| D.8 | Bornes et cas limites | À définir |


#### T007 · SYS-002.D.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T007`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t007) — export ligne 1694; réponse ligne 1706.

**Prescription approuvée (début) :** Validation SYS-002.D.1 : modèle B. Précisions et modifications : Le mode hybride est très bien.
Je vais rajouter des caractéristiques propres au jeu officiel afin qu'on puisse être sur les mêmes bases.
Attributs basiques :
PV, ATQ,  DEF, Vitesse d'ATQ
Attributs avancés : 
Coup critique, Ignorance de coup critique, Dégâts critique, Résistance critique, Combo, Ignorance du combo, Contre attaque, Ignorance de contre attaque, Etourdissement, Ignorance d'étourdissement, Evasion, Ignorance d'évasion, Régénération, Ignorance de régénération, En vol, Ignorance d'en vol, Coefficient d'ATQ normale, Réduction des dégâts d'ATQ normale, Coefficient de combo, Réduction des dégâts de combo, Coefficient de contre attaque, Réduction des dégâts de contre attaque, Coup critique de compétence, Ignorance du coup critique de compétence, Dégâts critiques de compétence, Dégâts de compétence, Réduction des dégâts de compétence, Dégâts de boss, Réduction des dégâts de boss, Dégâts d'Acolyte, Réduction des dégâts d'acolyte, Taux de guérison, Quantité de guérison, Perforation d'armure, Ignorance de perforation d'armure, Blocage, ignorance de blocage, Inspiration des acolytes, Ignorance de l'inspiration des Acolytes, Résistance des Acolytes, Ignorance de résistance des acolytes, Pénétration, Anti pénétration, Pénétration de compétence, Pénétration d'acolyte, Anti pénétration d'acolyte, Réduction des dégâts, Bonus de PV, Bonus d'ATQ, Bonus de Def, Bonus de vitesse d'ATQ, Augmentation des dégâts finales, Réduction des dégâts finale
Attributs finaux :
PV finaux, ATQ finale, DEF finale, Vitesse d'ATQ…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T007`.


### 02 - Défense, pénétration et résistances

#### T008 · SYS-002.D.2.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T008`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t008) — export ligne 2076; réponse ligne 2081.

**Prescription approuvée :** Validation SYS-002.D.2.1 : modèle B. Constante K : dynamic. Précisions : Aucune

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Modèle | Rendement décroissant |
| Constante K | À déterminer expérimentalement |
| DEF effective minimale | 0 |
| Mitigation | Calcul en précision flottante |
| Arrondi | À l'application finale des dégâts |
| Plafond de mitigation | Aucun plafond arbitraire à ce stade |


#### T009 · SYS-002.D.2.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T009`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t009) — export ligne 2449; réponse ligne 2454.

**Prescription approuvée :** Validation SYS-002.D.2.2 : modèle DEF = keep ; cumul pénétration = multiplicative ; ajout anti-pénétration compétence = oui ; perforation armure = instant

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Modèle de défense | Rendement décroissant |
| Pénétration générale | Cumul multiplicatif |
| Pénétration de compétence | Cumul multiplicatif |
| Pénétration d'acolyte | Cumul multiplicatif |
| Anti-pénétration de compétence | Ajoutée |
| Perforation d'armure | Effet instantané |


#### T010 · SYS-002.D.2.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T010`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t010) — export ligne 2755; réponse ligne 2760.

**Prescription approuvée :** Validation SYS-002.D.2.3 : cumul des résistances = multiplicative ; portée perforation armure = specific ; dégâts de boss = separate

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision retenue |
|--------|--------|
| Cumul des résistances | Multiplicatif |
| Portée de la perforation d'armure | Résistances spécifiques uniquement |
| Dégâts de boss | Modificateur indépendant |
| Réduction globale | Couche indépendante |
| Réduction finale | Couche indépendante |


### 03 - Critiques

#### T011 · SYS-002.D.3.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T011`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t011) — export ligne 3025; réponse ligne 3030.

**Prescription approuvée :** Validation SYS-002.D.3.1 : critique général = subtract ; critique compétence = separate ; plafond = 100 ; héritage du type de dégâts = type

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Critique général | Soustraction des attributs antagonistes |
| Critique de compétence | Système indépendant |
| Plafond du taux critique | 100 % |
| Compétence avec type de dégâts spécifique | Hérite du système critique de son type |
| Plancher du taux critique | 0 % |


#### T012 · SYS-002.D.3.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T012`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t012) — export ligne 3303; réponse ligne 3308.

**Prescription approuvée :** Validation SYS-002.D.3.2 : dégâts critiques généraux = reference ; dégâts critiques compétence = power ; portée résistance critique = general ; multiplicateur minimal = 150 ; ordre application = before_final

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Dégâts critiques généraux | Formule de référence |
| Dégâts critiques de compétence | Formule avec puissance 0,98 |
| Résistance critique | S'applique aux critiques généraux |
| Multiplicateur critique minimal | 1,5 |
| Ordre d'application | Après résistances spécifiques, avant modificateurs finaux |


### 04 - Évasion

#### T013 · SYS-002.D.4.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T013`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t013) — export ligne 3614; réponse ligne 3622.

**Prescription approuvée :** Validation SYS-002.D.4.1 : formule évasion = reference ;  plafond = 100 ; précision = remove ; effets après esquive = on_hit ; observations = Il faudrait vérifier comment fonctionne l'évasion dans le jeu officiel.
La définition de l'évasion dans le jeu est : Chance d'esquiver l'ATQ normale lors de l'ATQ normale subit.
Concernant l'ignorance de l'évasion : Réduit le taux d'évasion lors de l'ATQ normale.
Dans le jeu officiel, le taux de l'évasion va au-delà de 100%

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Formule mathématique | Modèle de référence, puissance 0,9, à vérifier |
| Portée | Attaque normale subie uniquement |
| Précision | Non intégrée |
| Effets après esquive | Aucun effet nécessitant un impact |
| Plafond de la statistique | Aucun plafond à 100 % |
| Valeur d'évasion | Peut dépasser 100 % |


#### T014 · SYS-002.D.4.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T014`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t014) — export ligne 3873; réponse ligne 3878.

**Prescription approuvée :** Validation SYS-002.D.4.2 : portée = expanded ; plafond PvE = 100 ; plafond PvP = 80 ; formule = reference

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Portée de l'évasion | Attaques normales, combos, contre-attaques et acolytes |
| Plafond effectif PvE | 100 % |
| Plafond effectif PvP | 80 % |
| Formule | Référence, puissance 0,9 |
| Statistique brute | Peut dépasser 100 % |
| Précision | Non utilisée |


### 05 - Vitesse et cadence d’attaque

#### T015 · SYS-002.D.5.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T015`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t015) — export ligne 4147; réponse ligne 4152.

**Prescription approuvée :** Validation SYS-002.D.5.1 : unité = aps ; portée = basic_skill ; cumul des bonus = hybrid ; plafond = none

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Unité | Attaques par seconde (APS) |
| Portée | Attaques normales et exécution des compétences |
| Cooldowns | Indépendants de la vitesse d'attaque |
| Cumul des bonus | Hybride |
| Plafond maximal | Aucun plafond artificiel |


#### T016 · SYS-002.D.5.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T016`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t016) — export ligne 4558; réponse ligne 4563.

**Prescription approuvée :** Validation SYS-002.D.5.2 : première attaque = immediate ; modification dynamique = preserve ; début cooldown = activation ; exécution compétence = inverse ; verrou compétences = parallel ; précision temporelle = microseconds

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Première attaque | Immédiate dès que la cible est à portée |
| Modification dynamique | Préservation de la progression du cycle |
| Début du cooldown | Au déclenchement |
| Exécution des compétences | Inversement proportionnelle à la vitesse |
| Exécution simultanée | Plusieurs compétences en parallèle |
| Précision temporelle | Microsecondes entières, 64 bits |


### 06 - Agrégation, groupes et modificateurs

#### T017 · SYS-002.D.6.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T017`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t017) — export ligne 4876; réponse ligne 4881.

**Prescription approuvée :** Validation SYS-002.D.6.1 : groupes = explicit ; bonus plats = before ; cumul pourcentages = group ; groupe manquant = reject

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Groupes de cumul | Explicitement configurés |
| Bonus plats | Avant les bonus en pourcentage |
| Bonus d'un même groupe | Additifs |
| Groupes indépendants | Multiplicatifs |
| Groupe manquant | Rejet du modificateur |


#### T018 · SYS-002.D.6.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T018`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t018) — export ligne 5222; réponse ligne 5227.

**Prescription approuvée :** Validation SYS-002.D.6.2 : cumul attaque/cible = multiply ; cumul résistances même famille = family ; position critique = after_global ; augmentation/réduction finale = independent

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Bonus attaque / cible | Multiplicatifs indépendants |
| Sources d'une même résistance | Additives |
| Familles de résistances différentes | Multiplicatives |
| Position du critique | Après résistances globales |
| Augmentation finale | Multiplicateur indépendant |
| Réduction finale | Multiplicateur indépendant |


#### T019 · SYS-002.D.6.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T019`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t019) — export ligne 5632; réponse ligne 5637.

**Prescription approuvée :** Validation SYS-002.D.6.3 : OVERRIDE = base ; conflit même priorité = reject ; politique de cumul = explicit ; valeurs négatives = allow_clamp ; expiration = before ; UNIQUE_SOURCE = refresh ; observations = Afin d'être en accord, si plusieurs bonus se succèdent par rapport au même attribut, il doivent s'additionner, pas seulement choisir le dernier ou le plus élevé. Par exemple si une compétence applique +5% de vitesse d'attaque pendant 3 secondes et qu'une autre compétence simultanément active +3% de vitesse d'attaque pendant 6 secondes, le bonus sera de 8% pendant 3 secondes puis redescendra à 3% pour les 3 secondes restantes. Est ce clair ?

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| `OVERRIDE` | Remplace la valeur de base |
| Conflit de priorité identique | Rejet |
| Politique de cumul | Obligatoire et explicite |
| Valeurs négatives | Autorisées, avec contraintes par attribut |
| Expiration | Avant les événements au même timestamp |
| `UNIQUE_SOURCE` | Actualisation de la durée |


#### T020 · SYS-002.D.6.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T020`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t020) — export ligne 5990; réponse ligne 5995.

**Prescription approuvée :** Validation SYS-002.D.6.4 : résistances négatives = clamp ; dégâts minimum = zero ; arrondi = floor ; application contraintes = final ; dénominateur critique invalide = reject ; observations = Je ne sais plus si j'ai déjà parlé des caractéristiques : Combo d'Acolyte et Coup critique d'Acolyte qui sont également des caractéristiques comme le Combo, la Contre attaque, le Coup critique etc

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Résistances négatives | Ramener la valeur effective à 0 % |
| Résistance maximale | 100 % |
| Dégâts minimum | 0 |
| Arrondi des dégâts | `floor()` |
| Application des contraintes | Après résolution des modificateurs |
| Dénominateur critique invalide | Rejet de la configuration |


### 07 - Référentiel des statistiques

#### T021 · SYS-002.D.7.1

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T021`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t021) — export ligne 6395; réponse ligne 6408.

**Prescription approuvée :** SYS-002.D.7.1 — Validation du référentiel : nature combo/critique acolyte = bonus ; attributs antagonistes = unknown ; dégâts critiques acolyte = unknown ; autres caractéristiques = Je vais donner plus de précision sur la synergie de ces deux attributs.
La synergie entre le combo d'acolyte et le coup critique d'acolyte repose sur la façon dont les compagnons (acolytes) infligent des dégâts.

Le combo d'acolyte :
Il donne une chance aux acolytes d'effectuer une attaque supplémentaire (un combo) après leur coup initial.
Le coup critique d'acolyte :
Il permet aux attaques des acolytes d'infliger des dégâts critiques (multipliés par vos dégâts de coup critique d'acolyte)
Lorsqu'un acolyte attaque, il peut déclencher un coup critique, puis éventuellement enchaîner avec un combo (qui peut lui aussi être critique selon les statistiques).
Pour qu'un build "acolyte" soit redoutable, il ne faut pas négliger l'attaque globale, car les dégâts de base des acolytes dépendent directement de notre puissance d'attaque générale et des multiplicateurs spécifiques (dégâts d'acolyte purs multipliés par vos bonus)


#### T022 · SYS-002.D.7.3

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T022`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t022) — export ligne 6864; réponse ligne 6877.

**Prescription approuvée :** SYS-002.D.7.3 — Validation globale : ATQ acolyte = final ; coefficient acolyte = individual ; critiques = per_hit ; enchaînement combo = single ; architecture = approve ; observations = Je vais rajouter une précision concernant les acolytes, qu'il faudra certainement approfondir plus tard.
Les acolytes sont des compagnons qui accompagnent et soutiennent le personnage dans ses combats (PvE ou PvP). 
Les acolytes possèdent également un niveau, allant du niveau 1 à 200.
Pour faire évoluer et monter en niveau les acolytes, il faut accumuler des doublons en effectuant des invocations d'acolyte.
Chaque acolyte possède des caractéristiques qui lui sont propres indépendamment des caractéristiques (que nous connaissons déjà) du personnage.
L'acolyte possède :
Coefficient de dégâts, Vitesse d'attaque, Coup critique, Dégâts critique, Combo, Coefficient de combo, Ignorance d'évasion.
Chaque acolyte possède également un effet de déploiement qui lui est propre (à définir plus tard).
Ils possèdent différents niveaux de rareté (rares, excellents, épiques, mythiques, etc.), les plus rares offrant des compétences uniques très puissantes (boucliers, soin, boosts massifs de stats etc.)

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| ATQ utilisée pour les dégâts des acolytes | `final_attack` du propriétaire |
| Coefficient de dégâts | Individuel à chaque acolyte |
| Déclenchement critique | Tirage indépendant par attaque |
| Déclenchement du combo | Un seul combo supplémentaire par attaque initiale |
| Architecture Character Stats Engine | Approuvée |


### 08 - Mécaniques de combat additionnelles

#### T024 · SYS-002.D.8.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T024`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t024) — export ligne 7591; réponse ligne 7596.

**Prescription approuvée :** Validation SYS-002.D.8.1 : portée du combo = normal ; formule ignorance = subtract ; nombre de combos = single ; condition = landed ; temporalité = immediate ; base dégâts = attack_times_coefficient

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Portée du déclenchement | Attaques normales uniquement |
| Calcul du taux | Soustraction directe |
| Nombre de combos | Un par attaque initiale |
| Condition | Attaque initiale non esquivée |
| Temporalité | Immédiatement après l'attaque initiale |
| Base des dégâts | ATQ finale × coefficient de combo |


#### T025 · SYS-002.D.8.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T025`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t025) — export ligne 7955; réponse ligne 7965.

**Prescription approuvée :** Validation SYS-002.D.8.2 : portée = direct ; condition = positive_damage ; ignorance = subtract ; nombre = per_event ; base dégâts = attack_coefficient ; critique = general ; évasion = yes ; temporalité = immediate ; observations = • Les attaques normales : Chaque attaque de base de l'adversaire lance un jet de probabilité selon votre taux de contre-attaque.
• Les attaques de combo : Chaque coup supplémentaire issu d'un combo ennemi compte comme une attaque distincte et peut déclencher une riposte.
• Les compétences actives : Les compétences qui infligent des dégâts directs à votre personnage activent également votre probabilité de contre-attaque.
• Les attaques d'acolytes : Les coups portés directement par les familiers adverses peuvent déclencher vos ripostes.
L'évasion (Esquive) : Si vous esquivez une attaque grâce à votre statistique d'évasion, la contre-attaque ne se déclenche pas dans les mécaniques standards, car vous n'avez pas été touché (sauf effet de classe très spécifique).
Les boucliers : Si vous absorbez un coup grâce à un bouclier, l'attaque est tout de même comptabilisée comme reçue et peut donc déclencher votre contre-attaque

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Portée | Toutes les attaques directes |
| Condition | Attaque reçue et non esquivée |
| Ignorance | Soustraction directe |
| Nombre | Une contre-attaque par événement |
| Base des dégâts | ATQ finale × coefficient de contre-attaque |
| Critique | Système critique général |
| Évasion | Possible sur la contre-attaque |
| Temporalité | Immédiatement après l'attaque reçue |
| Contre-attaque récursive | Interdite |


#### T026 · SYS-002.D.8.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T026`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t026) — export ligne 8318; réponse ligne 8323.

**Prescription approuvée :** Validation SYS-002.D.8.3 : signification stun_ignore = reduce ; portée = direct ; condition = landed ; actions bloquées = all_actions ; durée = effect_defined ; réapplication = refresh

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Ignorance d'étourdissement | Réduction directe du taux adverse |
| Portée | Toutes les attaques directes |
| Condition | Attaque non esquivée |
| Actions bloquées | Toutes les actions offensives et défensives |
| Durée | Définie par l'effet |
| Réapplication | Actualisation de la durée |


#### T027 · SYS-002.D.8.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T027`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t027) — export ligne 8654; réponse ligne 8667.

**Prescription approuvée :** Validation SYS-002.D.8.4 : ignorance = subtract ; portée = direct ; effet = verify ; vulnérabilité = vulnerable ; durée = effect ; réapplication = refresh ; interaction étourdissement = coexist ; observations = Il faudrait changer le nom de cette caractéristique, je ne la trouve pas très clair au premier abord.
Le mécanisme d'en vol (ou lancement en l'air) est un effet de contrôle de foule qui projette brièvement la cible dans les airs, interrompant toutes ses actions.

Fonctionnement et effets en combat

• Interruption totale (Micro-étourdissement) : Lorsqu'un ennemi est projeté en vol, il est incapable d'attaquer, de déclencher des combos, de contre-attaquer ou d'activer ses compétences tant qu'il est en l'air.
• Durée très courte : Contrairement à l'étourdissement classique des Mages qui dure plusieurs secondes, le lancement en vol est très bref.
• Contre-mesure contre la résistance à l'étourdissement : Le lancement en vol est considéré comme une mécanique distincte de l'étourdissement. Il ignore la statistique de « Résistance à l'étourdissement » de l'adversaire, ce qui le rend redoutable en PvP.
• Réinitialisation des animations : En plus de faire gagner de précieuses fractions de seconde, la projection brise le rythme d'attaque de l'adversaire et retarde le rechargement de ses compétences actives

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Calcul de l'ignorance | Soustraction directe |
| Portée | Toutes les attaques directes |
| Effet | Interruption totale des actions |
| Vulnérabilité | La cible reste attaquable |
| Durée | Très courte, définie par effet |
| Réapplication | Actualisation de la durée |
| Interaction avec étourdissement | Coexistence indépendante |
| Résistance à l'étourdissement | Ignorée |


#### T028 · SYS-002.D.8.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T028`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t028) — export ligne 9067; réponse ligne 9079.

**Prescription approuvée :** Validation SYS-002.D.8.5 : portée = direct ; ignorance = subtract ; conséquence = reduce ; quantité bloquée = fixed ; fréquence = per_hit ; effets secondaires = hit_effects ; ordre de calcul = before_defense ; observations = le blocage (Block) est une statistique défensive avancée qui permet de réduire une partie des dégâts subis lors d'une attaque directe, et s'oppose directement à la statistique de perforation (Pierce).

Fonctionnement en combat

• Réduction des dégâts subis : Lorsqu'un blocage s'active face à une attaque ennemie, il diminue considérablement les dégâts finaux que vous recevez, ce qui vous permet de survivre beaucoup plus longtemps face aux classes à gros dégâts (DPS).
• Opposition Blocage vs Perforation : Le système fonctionne par comparaison entre votre statistique de Blocage et la statistique de Perforation (Pierce) de l'adversaire. Plus votre blocage est supérieur à sa perforation, plus le déclenchement et l'efficacité de la réduction sont élevés.
• Interactions avec les autres mécaniques : Contrairement à l'évasion qui annule totalement le coup (et empêche la contre-attaque), le blocage laisse l'attaque vous toucher avec des dégâts réduits. Cela permet aux Guerriers d'encaisser le coup tout en continuant de déclencher leurs contre-attaques.
• Limites face aux dégâts spéciaux : Le blocage est très efficace contre les attaques classiques, mais son impact est beaucoup plus faible contre les dégâts indexés sur un pourcentage de vos PV maximum

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Portée | Toutes les attaques directes |
| Ignorance de blocage | Soustraction directe |
| Conséquence | Réduction des dégâts |
| Réduction de base | Valeur fixe configurable |
| Fréquence | Un tirage par coup |
| Effets secondaires | Conservés |
| Ordre d'application | Avant défense et pénétration |


#### T029 · SYS-002.D.8.6

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T029`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t029) — export ligne 9497; réponse ligne 9509.

**Prescription approuvée :** Validation SYS-002.D.8.6 : unité = max_hp ; fréquence = periodic ; ignorance = subtract ; portée ignorance = continuous ; interaction guérison = separate ; contrôles = continue ; cumul = independent ; observations = la régénération (Regen) permet de récupérer des points de vie (PV) de façon passive et continue chaque seconde durant un combat.

Fonctionnement et mécanismes

• Soin par seconde : Contrairement au vol de vie ou aux soins déclenchés par vos attaques, la régénération restaure automatiquement un pourcentage de vos PV maximum chaque seconde.
• Aucune condition d'action : Vous continuez de regagner de la vie même lorsque vous êtes étourdi (Stun), projeté en l'air ou incapable d'attaquer.
• Synergie avec les PV maximum : Plus votre réserve totale de PV est élevée, plus le montant réel de soins récupéré à chaque seconde est important.
• Limite d'efficacité (Anti-soin) : En PvP, l'efficacité de la régénération diminue à mesure que le combat s'éternise (réduction progressive des soins dans le temps) et peut être réduite par des effets « anti-soin » adverses

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Unité | Pourcentage des PV maximum par seconde |
| Fréquence | Périodique, toutes les secondes |
| Ignorance de régénération | Soustraction directe |
| Portée | Continue pendant le combat |
| Interaction avec la guérison | Indépendante |
| Étourdissement | Régénération maintenue |
| Projection aérienne | Régénération maintenue |
| Cumul des sources | Instances indépendantes et cumulatives |


#### T030 · SYS-002.D.8.7

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T030`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t030) — export ligne 9841; réponse ligne 9857.

**Prescription approuvée (début) :** Validation SYS-002.D.8.7 : inspiration = stats ; ignorance inspiration = reduce ; résistance = damage ; ignorance résistance = reduce ; portée = unknown ; modèle mathématique = unknown ; observations = la caractéristique d'inspiration des acolytes correspond à une attaque spéciale déclenchée par vos acolytes en plus de leurs attaques normales et de leurs compétences passives.
Mécanisme de déclenchement et effets
- Une attaque de groupe ou renforcée : Lorsqu'un acolyte déclenche son inspiration, il effectue une frappe spéciale dont les dégâts sont calculés à partir de votre statistique d'attaque globale et amplifiés par le multiplicateur d'inspiration d'acolyte.
- Condition d'activation : L'inspiration fonctionne sur un système de probabilité par attaque ou de jauge d'énergie liée aux coups portés par vos acolytes. Plus la vitesse d'attaque de vos acolytes est élevée, plus ils accumulent rapidement les conditions nécessaires pour déclencher cette inspiration.
- Synergie avec la classe Dompteur : La branche du Dompteur (Beast Master / Tamer) repose entièrement sur ce mécanisme. Ses compétences actives et ses passifs d'éveil augmentent directement le taux d'inspiration, les dégâts d'inspiration et permettent à tous vos acolytes équipés de déclencher simultanément un état d'excitation.
- Interaction avec les critiques et combos d'acolytes : Une attaque d'inspiration peut également bénéficier d'un coup critique d'acolyte, créant des pics de dégâts massifs en combat.

la statistique Ignorance de l'inspiration d'acolyte (Ignore Pal Inspire) est une caractéristique défensive de…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T030`.


### 09 - Modèle des acolytes et combat

#### T032 · SYS-002.D.9.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T032`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t032) — export ligne 10567; réponse ligne 10592.

**Prescription approuvée (début) :** Validation SYS-002.D.9.1 : gestion instances = separate ; doublons = shared_balance ; progression niveaux = individual ; courbes = rarity_curve ; influence rareté = capabilities ; effets déploiement = on_deploy ; runtime = snapshot ; observations = Les acolytes (Pals) sont classés selon 8 niveaux de rareté standard (du plus commun au plus rare), auxquels s'ajoute une catégorie spéciale pour les événements exclusifs.

Les 8 raretés principales (du plus faible au plus puissant)

• Normal (Gris / Blanc) : Les acolytes de base obtenus dès le début du jeu, offrant de très faibles bonus.
• Unique (Vert) : La deuxième catégorie de départ, utile uniquement lors des toutes premières heures de progression.
• Bien / Supérieur (Bleu) : Permet d'obtenir les premiers petits effets passifs utiles en début de partie.
• Rare (Violet) : Introduit des effets de déploiement plus intéressants pour commencer à orienter votre style de jeu.
• Mythique (Orange) : Marque un cap important avec des bonus nettement plus élevés et des synergies de classe plus marquées.
• Épique (Rouge) : Des acolytes très puissants qui constituent la base des équipes de milieu et fin de jeu.
• Légendaire (Doré / Jaune) : Offrent des capacités passives majeures et de gros multiplicateurs de statistiques.
• Immortel (Rose / Arc-en-ciel) : Le rang ultime des invocations classiques, doté des meilleurs effets de combat et des plus hauts bonus passifs permanents.

Catégorie supplémentaire

• Exclusif / Collab (Spécial) : Certains acolytes spéciaux (comme ceux issus des collaborations ou événements temporaires) disposent de…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T032`.

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Gestion des instances | Instances individuelles |
| Doublons | Solde partagé par type |
| Progression | Individuelle |
| Courbes | Dépendantes de la rareté |
| Influence de la rareté | Statistiques et compétences |
| Effets de déploiement | Conditionnés par l'équipement |
| Runtime | Snapshot actualisable |


#### T033 · SYS-002.D.9.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T033`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t033) — export ligne 11027; réponse ligne 11046.

**Prescription approuvée (début) :** Validation SYS-002.D.9.2 : gestion instances = one_per_type ; ressources = duplicates_only ; coût = rarity_table ; statistiques évolutives = all_seven ; courbes = piecewise ; montée de niveau = multi ; doublons niveau 200 = retain ; bonus permanents = unknown ; observations = Je vais clarifier :
un acolyte monte du niveau 1 au niveau 200 exclusivement en consommant des exemplaires identiques (doublons) obtenus lors de vos invocations au portail.

La montée en niveau (1 à 200) et consommation des doublons

• Déblocage initial : Le tout premier exemplaire tiré au portail débloque l'acolyte au niveau 1.
• Coût progressif en doublons : Pour passer au niveau supérieur, il faut accumuler un nombre précis de cartes du même acolyte. Ce coût commence très bas (2 ou 3 doublons aux tout premiers niveaux) et augmente progressivement par paliers jusqu'au niveau 200.
• Bouton « Amélioration rapide » : Dès que vous possédez assez de doublons pour un ou plusieurs paliers, un bouton d'amélioration globale permet de convertir automatiquement tous vos doublons disponibles en niveaux.
• Recyclage des doublons après le niveau 200 : Une fois qu'un acolyte atteint le niveau maximum (200), les doublons supplémentaires que vous continuez de tirer ne sont pas perdus. Le jeu les fusionne automatiquement pour générer des cartes d'acolytes de la rareté supérieure, ce qui accélère considérablement la montée des acolytes Mythiques, Légendaires et Immortels en fin de jeu.

L'évolution des caractéristiques à chaque niveau

• L'effet possédé (Bonus passif permanent) : À chaque niveau gagné, le pourcentage…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T033`.

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision définitive |
|--------|--------|
| Déblocage | Premier exemplaire obtenu au niveau 1 |
| Instance de progression | Une par type d'acolyte |
| Ressource | Doublons identiques exclusivement |
| Coût | Table par rareté et niveau |
| Progression | Individuelle, niveaux 1 à 200 |
| Courbes | Par paliers |
| Amélioration rapide | Plusieurs niveaux en une opération |
| Niveau maximal | 200 |
| Doublons après niveau 200 | Fusion automatique vers la rareté supérieure |
| Bonus permanents | Évoluent avec le niveau |


#### T034 · SYS-002.D.9.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T034`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t034) — export ligne 11498; réponse ligne 11519.

**Prescription approuvée (début) :** Validation SYS-002.D.9.3 : croissance des cinq caractéristiques = individual ; combinaison propriétaire/acolyte = explicit ; vitesse d'attaque = acolyte_only ; base bonus collection = base ; ciblage déploiement = per_effect ; actualisation snapshot = incremental ; cumul bonus collection = additive ; observations = Précision :
chaque caractéristique d'un acolyte possède sa propre règle d'évolution. Toutes les statistiques n'augmentent pas avec le niveau : certaines progressent linéairement, tandis que d'autres sont totalement figées ou dépendent uniquement de votre personnage principal.

Les caractéristiques qui évoluent avec le niveau (1 à 200)

• Le multiplicateur d'attaque de base (Dégâts de base) : C'est la statistique intrinsèque de combat qui augmente à chaque niveau gagné. Plus le niveau de l'acolyte est élevé, plus le pourcentage de votre attaque globale qu'il utilise pour frapper augmente.
• L'effet possédé (Bonus passif du compte) : À chaque montée de niveau, le pourcentage d'ATQ, de PV et de DÉF que l'acolyte apporte de manière permanente à votre personnage augmente progressivement.

Les caractéristiques intrinsèques fixes (qui n'évoluent pas avec le niveau)

• La vitesse d'attaque de base : Chaque acolyte possède une cadence de frappe propre (par exemple 1.0, 1.2 ou 1.5 attaque par seconde selon l'espèce) qui reste strictement identique du niveau 1 au niveau 200. Pour l'augmenter, il faut passer par la classe Dompteur d'Âmes, les reliques ou l'équipement.
• Les valeurs numériques du passif de déploiement : Les pourcentages ou durées inscrits dans la description…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T034`.

**Tableau de formalisation consécutive à la validation :**

| Caractéristique | Identifiant | Règle |
|--------|--------|--------|
| Vitesse d'attaque | `base_attack_speed` | Fixe du niveau 1 au 200 |
| Valeurs des effets de déploiement | `deployment_effect_values` | Fixes du niveau 1 au 200 |


#### T035 · SYS-002.D.9.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T035`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t035) — export ligne 11949; réponse ligne 11968.

**Prescription approuvée (début) :** Validation SYS-002.D.9.4 : participation = all_five ; scheduler = independent ; première attaque = immediate ; ciblage = owner_target ; changement de cible = immediate ; contrôles propriétaire = independent ; coefficient combo = unknown ; portée = per_acolyte ; observations = Précisions :
la gestion des cadences (vitesse d'attaque et fréquence des compétences) des acolytes en combat repose sur une séparation nette entre leurs attaques de base et leurs compétences passives à temps de recharge.

1. La cadence des attaques de base

• Rythme individuel et indépendant : Chaque acolyte attaque automatiquement selon sa propre vitesse d'attaque de base (exprimée en attaques par seconde). Vos 5 familiers n'attaquent pas de manière synchronisée par défaut, chacun suivant son propre compteur interne dès le début du combat.
• Calcul des modificateurs de vitesse : La vitesse d'attaque finale d'un acolyte est égale à sa vitesse de base multipliée par vos bonus globaux de Vitesse d'attaque d'acolyte (provenant de l'équipement, de la recherche, des âmes martiales et de la classe Dompteur).
• Impact sur les déclenchements : Plus cette cadence est rapide, plus l'acolyte effectue de frappes par seconde, ce qui augmente mécaniquement le nombre d'occasions de déclencher un Combo d'acolyte, un Critique d'acolyte ou la jauge d'Inspiration.
• Immunité aux contrôles de foule : Contrairement à votre personnage principal qui arrête de frapper lorsqu'il est étourdi (Stun) ou projeté en l'air (En vol), vos acolytes ne sont pas affectés par les contrôles ennemis et maintiennent leur cadence d'attaque…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T035`.

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Participation | Les cinq acolytes équipés |
| Cadence | Scheduler indépendant par acolyte |
| Première attaque | Immédiate |
| Ciblage | Cible du propriétaire |
| Changement de cible | Immédiat, sans réinitialisation de cadence |
| Contrôles du propriétaire | Sans incidence sur les acolytes |
| Coefficient de combo | Non déterminé |
| Portée | Individuelle par acolyte |


#### T036 · SYS-002.D.9.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T036`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t036) — export ligne 12498; réponse ligne 12517.

**Prescription approuvée (début) :** Validation SYS-002.D.9.5 : déclenchement = per_acolyte ; événements éligibles = normal_combo ; portée jauge = unknown ; réinitialisation = unknown ; formule dégâts = unknown ; critiques = inherited_per_hit ; ignorance inspiration = subtract ; simultanéité = independent ; interaction combo = unknown ; excitation Dompteur = tamer_effect ; observations = Précisions : 
l'inspiration fonctionne par un double mécanisme probabiliste et cumulatif lié aux attaques normales de vos acolytes.

Les étapes du déclenchement

• Jet de probabilité sur attaque normale. À chaque attaque de base effectuée par un acolyte, le jeu réalise un tirage basé sur votre statistique de Taux d'inspiration d'acolyte (Pal Inspire Rate).
• Activation de l'état d'inspiration. Si le tirage réussit, l'acolyte entre instantanément en état d'inspiration et exécute une frappe spéciale dont les dégâts sont multipliés par votre statistique de Dégâts d'inspiration.
• Interdiction de chaîne (Non-récursivité). Une attaque déclenchée par l'inspiration ne peut pas déclencher un combo d'acolyte ni réactiver une nouvelle inspiration sur le même coup.
• Déclenchement forcé par compétences actives. La branche de classe Dompteur (Beast Master / Tamer) dispose de compétences actives et d'éveils qui court-circuitent le tirage aléatoire en forçant tous les acolytes équipés à entrer simultanément en état d'inspiration pendant une durée fixe.
• Résolution défensive (Opposition). Avant d'appliquer les dégâts finaux à l'ennemi, votre valeur d'inspiration est comparée à la statistique d'Ignorance de l'inspiration d'acolyte (Ignore…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T036`.


#### T037 · SYS-002.D.9.6

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T037`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t037) — export ligne 13043; réponse ligne 13048.

**Prescription approuvée :** Validation SYS-002.D.9.6 : activation déploiement = while_equipped ; séparation effets/compétences = separate ; exécution = automatic ; déclenchement = per_skill ; cooldowns = independent ; ciblage = per_skill ; simultanéité = parallel ; cumul = modifier_engine ; déblocage = definition

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Activation des effets de déploiement | Tant que l'acolyte est équipé |
| Séparation effets/compétences | Deux systèmes distincts |
| Exécution des compétences | Automatique |
| Déclenchement | Configurable individuellement |
| Cooldowns | Indépendants par compétence |
| Ciblage | Défini individuellement |
| Exécution simultanée | Autorisée |
| Cumul des effets | Modifier Engine SYS-002.D.6 |
| Déblocage des compétences | Définition de l'acolyte |


### 10 - Acolytes, progression, invocations et architecture

#### T039 · SYS-002.D.10.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T039`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t039) — export ligne 13897; réponse ligne 13910.

**Prescription approuvée :** Validation SYS-002.D.10.1 : acolytes identiques = unknown ; bonus collection = once_per_type ; recyclage niveau 200 = immediate ; profils exclusifs = explicit_profile ; emplacements vides = allowed ; multiplicité Runtime = per_slot ; observations = Précisions :
Il n'est pas possible d'équiper exactement le même acolyte plusieurs fois, mais vous pouvez équiper plusieurs acolytes d'une même famille (de raretés différentes).

Fonctionnement dans l'équipe de cinq

• Acolyte unique. Chaque carte d'acolyte possède un seul emplacement d'amélioration (les doublons tirés servent à monter son niveau) et ne peut occuper qu'une seule place dans votre formation.
• Familles d'acolytes (variantes de rareté). Une même espèce (comme les oiseaux, les cerfs, les chats ou les escargots) existe en plusieurs versions de rareté différente, et vous pouvez les placer ensemble dans votre équipe.
• Non-cumul des passifs identiques. Comme le soulignent les joueurs sur la communauté Reddit Legend of Mushroom, les effets passifs de la même famille ne se cumulent généralement pas et seul le bonus de l'acolyte ayant la plus haute statistique s'applique (à de rares exceptions près comme certains dragons).
• Priorité aux synergies. Il est donc préférable de varier les familles d'acolytes afin d'activer cinq bonus passifs distincts et adaptés à votre classe, comme détaillé dans le classement des acolytes sur Mobi.gg

**Tableau de formalisation consécutive à la validation :**

| Élément | Décision |
|--------|--------|
| Équipement d'un acolyte identique | Interdit |
| Équipement de variantes d'une même famille | Autorisé |
| Bonus de collection | Une fois par variante possédée |
| Recyclage au niveau 200 | Immédiat |
| Profils des acolytes exclusifs | Profil explicite |
| Emplacements vides | Autorisés |
| Runtime | Un par emplacement |
| Passifs familiaux identiques | Non cumulables par défaut |
| Sélection des passifs | Valeur effective la plus élevée |
| Exceptions familiales | Configurables explicitement |


#### T040 · SYS-002.D.10.1

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T040`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t040) — export ligne 14383; réponse ligne 14418.

**Prescription approuvée (début) :** Je veux rajouter d'autres précisions :

**les acolytes sont regroupés par espèces ou « familles » thématiques, chacune offrant un type de bonus passif spécifique à travers plusieurs paliers de rareté**.

Voici les principales familles d'acolytes et leurs effets associés en combat :

**Familles orientées attaque et critiques**

- **Oiseaux** (*Champignon Oiseau, Oiseau Anti-Pluie, Oiseau Azuré, Plumes de feu sombre*). Ils augmentent la vitesse d'attaque, les chances de combo ou les dégâts de combo.
- **Poules et Coqs** (*Poussin Éclos, Coq Combattant*). Ils renforcent les dégâts des attaques normales.
- **Cactus** (*Cactus Bébé, Cactus de Bête, Cactus dynamique*). Ils infligent des dégâts supplémentaires toutes les trois attaques normales.
- **Dragons** (*Dragon du Trésor, Dragon noir, Dragon de bonheur*). Ils améliorent les chances et les dégâts de coups critiques (attaques normales et compétences).
- **Pieuvres** (*Pieuvre de Pirate*). Elles augmentent les dégâts de combo et déclenchent des attaques supplémentaires tous les trois combos.

**Familles orientées compétences et contrôle**

- **Hydro-Elfes / Blobs** (*Hydro-Elfe Rose, Hydro-Elfe Belliqueux*). Ils accélèrent la régénération d'énergie des compétences actives.
- **Chats** (*Chaton, Chat Noir, Chat Magicien*). Ils prolongent la durée d'étourdissement des ennemis ou augmentent les dégâts de contre-attaque selon leur variante.
- **Escargots** (*Petit Escargot Jaune, Escargot Épineux, Escargot Vert*). Ils ralentissent la vitesse de déplacement et d'attaque des ennemis.
- **Elfes de Neige / Yétis** (*Pudding de Neige,…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T040`.


#### T042 · SYS-002.D.10.2.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T042`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t042) — export ligne 15172; réponse ligne 15197.

**Prescription approuvée (début) :** Validation SYS-002.D.10.2.1 : courbe de coûts = stepwise ; monotonie coûts = non_decreasing ;  monotonie caractéristiques = non_decreasing ; coefficient combo = unknown ; profils de croissance = individual_reusable ; précision numérique = full_precision ; observations = Précisions :
La progression des acolytes (et des compétences) suit un modèle mathématique par paliers sur 200 niveaux, combinant un coût en doublons croissant et une courbe de croissance des statistiques qui s'accélère fortement à haut niveau.

1. Structure des coûts en doublons (Niveaux 1 à 200)

• Progression par paliers. Le nombre de copies (doublons) requises pour monter d'un niveau augmente par tranches de niveaux plutôt que de façon strictement linéaire à chaque niveau.
• Premiers niveaux (1 à 50). Les premiers paliers ne demandent que 2 à 5 doublons par niveau, ce qui permet de monter rapidement les raretés communes (Gris, Vert, Bleu) via les invocations.
• Milieu de courbe (51 à 150). Le coût grimpe progressivement par tranches (passant autour de 10, 15, puis 20 à 30 doublons par niveau), créant le premier goulot d'étranglement sur les raretés Violet et Jaune.
• Derniers paliers (151 à 200). Les ultimes niveaux exigent plusieurs dizaines de doublons par niveau (pouvant atteindre 40 à 50 copies sur les derniers paliers), portant le total cumulé à plusieurs milliers de copies pour atteindre le niveau 200.

2. Courbe de croissance des statistiques (Effet possédé vs équipé)

• Double impact statistique. Chaque niveau gagné augmente à la fois les dégâts de base de l'acolyte en combat et son bonus passif…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T042`.


#### T043 · SYS-002.D.10.2.1

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T043`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t043) — export ligne 15627; réponse ligne 15643.

**Prescription approuvée :** Précisions :

**Non, les compétences individuelles des acolytes n'ont pas de progression indépendante de niveau 1 à 200.** Un acolyte ne possède qu'une seule jauge de niveau globale (de 1 à 200) qui affecte uniquement ses dégâts de base et son bonus passif « Possédé ». 

**Distinction entre le niveau de l'acolyte et son effet**

- **Un seul niveau global par acolyte.** Vous améliorez l'acolyte dans son ensemble via ses doublons, sans jamais avoir à monter une compétence séparée sur sa fiche.
- **Effet de déploiement fixe.** Le bonus spécial d'un acolyte lorsqu'il est équipé dans l'équipe (par exemple l'augmentation du taux de combo, la durée d'étourdissement ou la régénération de PV) reste identique du niveau 1 au niveau 200.
- **Évolution liée au niveau global.** Monter de niveau (de 1 à 200) augmente uniquement le multiplicateur de dégâts des attaques de l'acolyte en combat ainsi que son bonus permanent « Possédé » (PV, Attaque ou Défense).
- **Ne pas confondre avec les compétences du personnage.** Les **compétences actives** de votre champignon (équipées dans les 5 emplacements de sorts) suivent quant à elles une progression séparée de niveau 1 à 200 via leurs propres tirages et doublons.

Pour approfondir le fonctionnement des tirages et des améliorations, vous pouvez consulter le guide dédié sur [**Guides by Grace**](https://guidesbygrace.uk/pals-skills)

**Tableau de formalisation consécutive à la validation :**

| ID | Décision | État |
|--------|--------|--------|
| PROG-009 | Niveau global unique par acolyte | (Validé) |
| PROG-010 | Deux catégories de sorties évolutives | (Validé) |
| PROG-011 | Effets de déploiement fixes | (Validé) |
| PROG-012 | Compétences d'acolytes sans progression propre | (Validé) |
| PROG-013 | Progression indépendante des compétences du personnage | (Validé) |
| PROG-014 | Portails et ressources distincts | (Validé) |


#### T044 · SYS-002.D.10.2.1

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T044`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t044) — export ligne 15862; réponse ligne 15887.

**Prescription approuvée (début) :** Précisions : 

**Dans la pratique (et comme observé dans *Legend of Mushroom*), les paliers de niveaux sont communs à toutes les raretés, mais chaque rareté possède sa propre échelle de coûts en doublons et ses propres taux de chute pour équilibrer la progression.**

Si vous concevez un système similaire (game design) ou cherchez à comprendre la logique mathématique derrière cette structure, voici pourquoi les paliers communs avec coûts différenciés s'imposent face aux paliers variables :

**1. Pourquoi garder des frontières de paliers communes (1–50, 51–150, 151–200)**

- **Lisibilité et repères cognitifs.** Le joueur assimile rapidement qu'un cap (comme le niveau 50, 100 ou 150) marque un changement de rythme universel, quelle que soit la carte consultée.
- **Alignement des courbes de puissance.** Garder les mêmes seuils permet de synchroniser les pics de statistiques passives (« Possédé ») entre les raretés communes et les raretés mythiques, facilitant l'équilibrage global du jeu.
- **Simplicité d'implémentation et de maintenance.** Une seule table de tranches de niveaux évite de multiplier les formules complexes et réduit les risques d'erreurs d'équilibrage lors de l'ajout d'une nouvelle rareté.

**2. Comment différencier les raretés sans changer les paliers**

- **Multiplicateur de coût par rareté.** Bien que les tranches de niveaux soient identiques, le nombre de doublons requis par niveau est ajusté selon la rareté (une rareté Commune demandera plus de copies par palier pour compenser sa grande abondance au tirage, tandis qu'une rareté Immortelle/Rose demandera…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T044`.


#### T045 · SYS-002.D.10.2.1.C.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T045`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t045) — export ligne 16172; réponse ligne 16185.

**Prescription approuvée :** Validation SYS-002.D.10.2.1.C.2 : sous-paliers = shared ; multiplicateur = global ; courbe de référence = lookup ; fusion Immortel = terminal ; observations = Précisions :
Oui, au sommet de la rareté Immortelle (Rose), il n'existe plus de palier supérieur vers lequel fusionner. Une fois qu'un acolyte ou une compétence (celles du personnage) Immortelle atteint le niveau 200 (MAX), les doublons supplémentaires s'accumulent dans votre inventaire sans conversion automatique.

Gestion des doublons au plafond Immortel

• Arrêt de la chaîne de synthèse. La mécanique de fusion (3 doublons de niveau 200 contre 1 exemplaire aléatoire de la rareté supérieure) s'arrête dès que les cartes Rouges (Mythiques/Exotiques) fusionnent vers les cartes Roses (Immortelles).
• Conservation dans l'inventaire. Les copies excédentaires d'un acolyte Immortel déjà au niveau 200 restent stockées en réserve sur sa fiche, car le jeu ne propose pas de rareté supérieure invocables dans le portail classique.
• Intérêt stratégique continu. Même lorsqu'un ou plusieurs Immortels atteignent le niveau maximum, les fusions issues des raretés inférieures continuent d'alimenter les autres acolytes Immortels qui ne sont pas encore niveau 200.
• Utilité pour les événements. Continuer à invoquer et fusionner des doublons reste rentable durant les événements de type Sprint d'acolytes ou de compétences, car les points sont attribués au nombre de tirages effectués et non à l'utilisation des doublons

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Grandes phases | Communes aux raretés |
| Sous-paliers | Communs aux raretés |
| Multiplicateur | Global par rareté |
| Courbe de référence | Lookup table |
| Monotonie | Non décroissante |
| Arrondi | Ceiling |
| Fusion standard | 3:1 |
| Rareté terminale | Immortel |
| Doublons Immortels au niveau 200 | Conservation |
| Fusion des Immortels maxés | Désactivée |


#### T046 · SYS-002.D.10.2.1.C.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T046`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t046) — export ligne 16589; réponse ligne 16594.

**Prescription approuvée :** Validation SYS-002.D.10.2.1.C.3 : sous-paliers = approve ; coûts de référence = approve ; rareté de référence = normal_one ; ordre des multiplicateurs = non_increasing

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Valeur définitive |
|--------|--------|
| Nombre de sous-paliers | 11 |
| Frontières | Communes |
| Coûts de référence | Table validée |
| Rareté de référence | Normal |
| Multiplicateur Normal | 1,00 |
| Multiplicateurs suivants | Non croissants |
| Calcul | Multiplication puis plafond |
| Fusion | 3:1 |
| Rareté terminale | Immortel |


#### T047 · SYS-002.D.10.2.1.C.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T047`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t047) — export ligne 16812; réponse ligne 16846.

**Prescription approuvée (début) :** Validation SYS-002.D.10.2.1.C.4 : multiplicateurs = approve ; statut calibration = provisional ; observations = Précisions :
Dans Legend of Mushroom, les probabilités de gacha d'obtention des acolytes et des compétences évoluent selon le niveau de la machine d'invocation (de 1 à 15), atteignant un maximum de 0,04 % (1 chance sur 2 500) pour la rareté Immortelle.

1. Évolution des taux selon le niveau d'invocation (1 à 15)

Chaque tirage effectué fait progresser une jauge d'expérience propre au portail (Acolytes ou Compétences) afin de débloquer de meilleures probabilités :
• Niveaux 1 à 8 (Début de partie). Les chances se concentrent quasi exclusivement sur les raretés Grise (Commune), Verte et Bleue, avec l'apparition progressive du Violet et du Jaune.
• Niveaux 9 à 12 (Milieu de partie). Les raretés Orange et Rouge (Exotique/Mythique) deviennent accessibles, tandis que la rareté Rose (Immortelle) s'ouvre autour du niveau 11-12 avec un taux initial de 0,01 % (1 chance sur 10 000).
• Niveau 13. Le taux d'obtention d'un Immortel double pour passer à 0,02 % (1 chance sur 5 000).
• Niveau 15 (Plafond maximum). La machine atteint son rendement maximal avec 0,04 % de chance pour un Immortel (1 chance sur 2 500), environ 0,2 % à 0,5 % pour le Rouge, et une forte réduction du taux de cartes Grises au profit des raretés Bleues, Violettes et Jaunes.

2. Probabilité de cibler une carte précise

• Partage équitable au sein d'une rareté. Lorsqu'un tirage tombe sur une rareté donnée, le jeu sélectionne aléatoirement l'une des cartes disponibles dans ce palier (par exemple, avec 3 à 5…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T047`.

**Tableau de formalisation consécutive à la validation :**

| Propriété | Décision |
|--------|--------|
| Niveau initial | 1 |
| Niveau maximal | 15 |
| Expérience par tirage | 1 XP |
| Progression | Automatique |
| Machine acolytes | Indépendante |
| Machine compétences | Indépendante |
| Probabilités | Dépendantes du niveau |
| Garantie classique (Pity) | Absente |
| Sélection dans une rareté | Équitable |
| Option x35 | 35 tirages pour 30 tickets |
| Option x999 | Débloquée au niveau 15 |


#### T048 · SYS-002.D.10.2.1.D.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T048`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t048) — export ligne 17550; réponse ligne 17555.

**Prescription approuvée :** Validation SYS-002.D.10.2.1.D.1 : ordre XP/tirage = before_xp ; tirages groupés = sequential ; sélection pool = uniform_available ; profils XP = independent

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision validée |
|--------|--------|
| Ordre XP/tirage | `before_xp` |
| Tirages groupés | `sequential` |
| Sélection des cartes | `uniform_available` |
| Profils XP | `independent` |


#### T049 · SYS-002.D.10.2.1.E.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T049`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t049) — export ligne 17958; réponse ligne 17963.

**Prescription approuvée :** Validation SYS-002.D.10.2.1.E.1 :    nombre de bonus possédés = single_type ; valeurs initiales = first_anchor_positive


#### T051 · SYS-002.D.10.2.1

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T051`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t051) — export ligne 18706; réponse ligne 18728.

**Prescription approuvée (début) :** **Il n'existe pas de base de données publique listant les valeurs numériques exactes niveau par niveau (1, 50, 100, 150, 200) de chaque acolyte**, mais nous disposons de la structure complète d'une fiche type et des formules exactes qui régissent sa progression.

Voici toutefois comment se présente une **fiche technique complète d'acolyte** et comment évoluent ses deux valeurs chiffrées sur les paliers demandés :

**1. Anatomie d'une fiche d'acolyte**

Sur la carte d'un acolyte en jeu, on retrouve quatre éléments distincts :

- **Rareté et niveau actuel (1 à 200).** Indique le palier de couleur (de Gris à Rose/Immortel) et l'avancement vers le plafond.
- **Effet de déploiement (Statique).** Le bonus spécial actif uniquement lorsque l'acolyte est équipé dans l'équipe de cinq (par exemple : *Vitesse d'attaque +15 %* ou *Dégâts de combo +25 %*), dont la valeur est identique au niveau 1 et au niveau 200.
- **Coefficient de dégâts en combat (Évolutif).** Le pourcentage de l'attaque de votre personnage que l'acolyte inflige à chacune de ses propres attaques basiques (par exemple : *Inflige 45 % de votre ATQ en dégâts* au niveau 1).
- **Bonus « Possédé » (Évolutif et cumulatif).** Le pourcentage permanent d'ATQ, de PV ou de DÉF ajouté à votre personnage, actif en permanence même si l'acolyte reste dans votre inventaire.

**2. Courbe d'évolution sur les paliers (1, 50, 100, 150, 200)**

- **Progression linéaire par niveau.** Contrairement au coût en doublons qui grimpe par paliers, le **bonus « Possédé »** et le **coefficient de dégâts** augmentent d'un incrément fixe à chaque…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T051`.

**Tableau de formalisation consécutive à la validation :**

| Ancienne décision | Nouvelle décision |
|--------|--------|
| Dégâts : piecewise linear convex | Linear constant increment |
| Bonus possédé : piecewise exponential | Linear constant increment |
| Accélération des pentes | Supprimée |
| Cinq points d'ancrage | Points de contrôle d'une droite unique |
| Différenciation des raretés | Valeurs initiales et incréments propres |


#### T052 · SYS-002.D.10.2.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T052`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t052) — export ligne 19069; réponse ligne 19074.

**Prescription approuvée :** Oui je valide

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Description |
|--------|--------|
| `damage_base_range` | Coefficient initial attendu |
| `damage_increment_range` | Incrément de dégâts attendu |
| `owned_base_range` | Bonus possédé initial attendu |
| `owned_increment_range` | Incrément du bonus possédé attendu |


#### T053 · SYS-002.D.10.2.1.E.8

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T053`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t053) — export ligne 19279; réponse ligne 19284.

**Prescription approuvée :** Validation SYS-002.D.10.2.1.E.8 : politique de calibration = soft ; ordre de puissance = expected ; réutilisation des profils = same_rarity

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision définitive |
|--------|--------|
| Politique de calibration | `soft` |
| Ordre de puissance des raretés | `expected` |
| Réutilisation des profils | `same_rarity` |


#### T055 · SYS-002.D.10.2.2.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T055`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t055) — export ligne 19935; réponse ligne 19940.

**Prescription approuvée :** Validation SYS-002.D.10.2.2.1 : bonus possédés = additive_unique ; effets familiaux = max_group ; exceptions = explicit ; effets différents = independent

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Bonus possédés | `additive_unique` |
| Effets familiaux | `max_group` |
| Exceptions | `explicit` |
| Effets différents | `independent` |


#### T056 · SYS-002.D.10.2.2.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T056`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t056) — export ligne 20436; réponse ligne 20441.

**Prescription approuvée :** Validons le modèle A


#### T057 · SYS-002.D.10.2.2.6

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T057`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t057) — export ligne 20661; réponse ligne 20666.

**Prescription approuvée :** Je valide le modèle C


#### T058 · SYS-002.D.10.2.2.7

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T058`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t058) — export ligne 20950; réponse ligne 20955.

**Prescription approuvée :** Je valide également


#### T059 · SYS-002.D.10.3.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T059`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t059) — export ligne 21245; réponse ligne 21250.

**Prescription approuvée :** Validation du modèle A


#### T060 · SYS-002.D.10.3.1.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T060`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t060) — export ligne 21567; réponse ligne 21572.

**Prescription approuvée :** Je valide cette recommendaion

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Normalisation | `strict_100` |
| Rareté indisponible | `zero_probability` |
| Précision numérique | `full_precision` |


#### T061 · SYS-002.D.10.3.2.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T061`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t061) — export ligne 21909; réponse ligne 21914.

**Prescription approuvée :** Validation SYS-002.D.10.3.2.4 : stockage des seuils = cumulative_lookup ; expérience niveau 15 = retain_xp

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Stockage des seuils | `cumulative_lookup` |
| XP au niveau 15 | `retain_xp` |
| XP par tirage | \+1 |
| Ordre XP/tirage | `before_xp` |
| Tirages groupés | `sequential` |
| Portails | `independent` |
| Niveau maximum | 15 |


#### T062 · SYS-002.D.10.3.3.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T062`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t062) — export ligne 22266; réponse ligne 22271.

**Prescription approuvée :** Validation SYS-002.D.10.3.3.4 : atomicité = durable_sequential ; gestion tickets = reserve_full ; sélection fusion = uniform_available

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Atomicité | `durable_sequential` |
| Gestion des tickets | `reserve_full` |
| Sélection des fusions | `uniform_available` |


#### T063 · SYS-002.D.10.3.4.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T063`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t063) — export ligne 22550; réponse ligne 22555.

**Prescription approuvée :** Validation SYS-002.D.10.3.4.1 : niveau initial après fusion = level_one ; gestion des doublons = manual

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Niveau initial après fusion | `level_one` |
| Gestion des doublons | `manual` |


#### T064 · SYS-002.D.10.3.4.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T064`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t064) — export ligne 22884; réponse ligne 22889.

**Prescription approuvée :** Validation SYS-002.D.10.3.4.2 : catalogue = portal_catalog ;  exclusifs = explicit_only

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Catalogue de fusion | `portal_catalog` |
| Exclusifs / collaborations | `explicit_only` |
| Sélection | `uniform_available` |


#### T065 · SYS-002.D.10.3.4.2

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T065`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t065) — export ligne 23244; réponse ligne 23249.

**Prescription approuvée :** Je veux corriger un point, si une carte d'acolyte ou de compétence n'a pas été débloqué par le tirage, elle ne peut pas être obtenue par la fusion


#### T066 · SYS-002.D.10.3.5.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T066`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t066) — export ligne 23472; réponse ligne 23477.

**Prescription approuvée :** Validation SYS-002.D.10.3.5.1 : moment du débit = charge_on_start ; interruption = resume_required

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Réservation | `reserve_full` |
| Moment du débit | `charge_on_start` |
| Interruption | `resume_required` |
| Atomicité des tirages | `durable_sequential` |
| Remboursement automatique après démarrage | Non |


#### T067 · SYS-002.D.10.3.5.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T067`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t067) — export ligne 23775; réponse ligne 23780.

**Prescription approuvée :** Validation du modèle A

**Tableau de formalisation consécutive à la validation :**

| ID | Règle |
|--------|--------|
| FUS-017 | Déblocage initial par invocation uniquement |
| FUS-018 | Réévaluation automatique après nouveau déblocage |
| FUS-019 | Fusion immédiate si les conditions sont réunies |
| FUS-020 | Conservation des doublons si aucun candidat |
| FUS-021 | Aucun déblocage par fusion |
| FUS-022 | Aucun niveau transmis par fusion |
| FUS-023 | Conservation du niveau de la carte destination |
| FUS-024 | Immortel niveau 200 : aucune fusion supérieure |


#### T068 · SYS-002.D.10.3.5.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T068`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t068) — export ligne 23965; réponse ligne 23970.

**Prescription approuvée :** Je valide le modèle A

**Tableau de formalisation consécutive à la validation :**

| ID | Règle |
|--------|--------|
| FUS-025 | Priorité à la rareté la plus basse |
| FUS-026 | Départage par `card_id` |
| FUS-027 | Une fusion par itération |
| FUS-028 | Réévaluation après chaque fusion |
| FUS-029 | Aucun traitement des cartes Immortelles comme sources |
| FUS-030 | Aucune destination non débloquée |
| FUS-031 | Conservation des doublons non consommés |


#### T069 · SYS-002.D.10.3.6.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T069`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t069) — export ligne 24276; réponse ligne 24281.

**Prescription approuvée :** Validation SYS-002.D.10.3.6.1 : stratégie de tests = all_layers ; RNG = injectable_rng ; persistance = crash_recovery

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Stratégie | `all_layers` |
| Générateur aléatoire | `injectable_rng` |
| Persistance | `crash_recovery` |


#### T070 · SYS-002.D.10.3.6.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T070`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t070) — export ligne 24853; réponse ligne 24858.

**Prescription approuvée :** Je valide A


#### T071 · SYS-002.D.10.3.7.1

**Autorité :** `APPROBATION_CONTEXTUELLE` · **Traçabilité :** [`T071`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t071) — export ligne 25119; réponse ligne 25124.

**Prescription approuvée :** Oui

**Tableau de formalisation consécutive à la validation :**

| Propriété | Règle |
|--------|--------|
| Ordonnancement | FIFO |
| Priorité | Ordre d'acceptation |
| Exécution simultanée même portail | Interdite |
| Exécution simultanée portails différents | Autorisée |
| Réorganisation des commandes | Interdite |
| Reprise après interruption | Prioritaire |
| Suppression d'un lot payé | Interdite |


#### T072 · SYS-002.D.10.3

**Autorité :** `APPROBATION_CONTEXTUELLE` · **Traçabilité :** [`T072`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t072) — export ligne 25344; réponse ligne 25349.

**Prescription approuvée :** Parfait

**Tableau de formalisation consécutive à la validation :**

| Phase | Statut |
|--------|--------|
| Architecture fonctionnelle | (Terminée) |
| Contrats métier | (Validés) |
| Contrats mathématiques | (Spécifiés) |
| Calibration numérique | (À réaliser) |
| Conception technique détaillée | (Prochaine étape) |
| Implémentation | En attente |


#### T074 · SYS-002.D.10.4.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T074`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t074) — export ligne 25639; réponse ligne 25644.

**Prescription approuvée :** Validation du modèle A

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Architecture globale | `modular_monolith` |
| Organisation métier | `domain_driven_modules` |
| Architecture interne | `ports_and_adapters` |
| Communication intermodules | `explicit_interfaces` |
| Persistance | `shared_database` |
| Transactions | `local_atomic_transactions` |
| Interface graphique | `presentation_decoupled` |


#### T076 · SYS-002.D.10.4.2.1

**Autorité :** `APPROBATION_CONTEXTUELLE` · **Traçabilité :** [`T076`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t076) — export ligne 25916; réponse ligne 25921.

**Prescription approuvée :** Très bien faisons comme ça alors dans un premier temps

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Plateforme cible | `android_only` |
| Environnement de développement | `pc` |
| Moteur graphique | `unity_6` |
| Langage | `csharp` |
| Architecture | `modular_monolith` |
| Persistance | `sqlite` |
| Configuration | `json_versioned` |
| Exécution | `standalone_offline` |
| Extensibilité | `cross_platform_preserved` |


#### T077 · SYS-002.D.10.4.2.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T077`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t077) — export ligne 26194; réponse ligne 26199.

**Prescription approuvée :** Je valide. En parallèle j'ai installé Unity


#### T078 · SYS-002.D.10.4.2.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T078`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t078) — export ligne 26493; réponse ligne 26499.

**Prescription approuvée :** Je valide le modèle A.
Je souhaite apporter des informations concernant le système d'obtention des équipements ainsi que les équipements en eux même, sauf si tu possède déjà ces informations?


### 11 - Équipement, lampe magique, affixes et calibration

#### T080 · SYS-002.D.11.1

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T080`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t080) — export ligne 26650; réponse ligne 26689.

**Prescription approuvée (début) :** Système d'obtention de l'équipement :

**La Lampe Magique est le moteur central de votre progression dans *Legend of Mushroom*.** Elle fonctionne selon une boucle d'équipement et de recyclage qui fait évoluer à la fois le niveau de votre personnage et la rareté des objets générés. 

---

**1. Condensé des mécanismes de la Lampe Magique**

- **Double moteur de progression.** Le **niveau de votre champignon** fixe la puissance brute (statistiques de base) des objets générés, tandis que le **niveau de la lampe** contrôle la probabilité d'obtenir des raretés élevées.
- **Boucle de recyclage (Or et EXP).** Chaque charge de lampe génère une pièce d'équipement aléatoire. Vous l'équipez si elle est meilleure, ou vous la vendez instantanément pour gagner de **l'expérience** (montée de niveau du personnage) et des **pièces d'or** (indispensables pour améliorer la lampe). 
- **Segments d'amélioration.** Monter la lampe d'un niveau nécessite d'acheter plusieurs segments avec votre or, suivis d'un temps de construction réductible via des tickets d'accélération ou des publicités. 
- **Automatisation (Auto-Lamp).** Débloqué au **niveau 16 de personnage**, le mode automatique fait tourner la lampe en arrière-plan et s'arrête uniquement lorsqu'une pièce correspond à vos critères de rareté et de statistiques secondaires. 
- **Tirages multiples et bannissement.** Aux niveaux de lampe **16, 20 et 24**, vous débloquez l'ouverture simultanée de **6, 8 puis 10 lampes** à la fois. Aux niveaux **12, 20 et 26**, la fonction *Adjust* permet de bloquer jusqu'à **3 affixes indésirables**. 
- **Sources…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T080`.


#### T081 · SYS-002.D.11.1.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T081`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t081) — export ligne 26918; réponse ligne 26923.

**Prescription approuvée :** SYS-002.D.11.1.4 — Validation Adjust : progressive


#### T082 · SYS-002.D.11.1.5.1

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T082`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t082) — export ligne 27000; réponse ligne 27027.

**Prescription approuvée (début) :** **L'amélioration d'un niveau de lampe fonctionne par paliers intermédiaires (segments) achetés avec de l'or, suivis d'un minuteur de construction obligatoire avant de passer au niveau suivant.**

Voici le fonctionnement exact de chacun des quatre points :

**1. Nombre de segments par niveau**

- **Nombre variable selon le palier.** Chaque niveau de lampe est divisé en un certain nombre de segments (généralement entre **3 et 5 segments** selon le niveau), et ce nombre augmente à mesure que vous progressez vers les hauts niveaux. [[1](https://www.youtube.com/watch?v=_QSsOBihZb0\&t=36)]
- **Exemple concret.** Au niveau 23, la barre de progression se divise en plusieurs segments individuels (coûtant chacun plus d'un million d'or) avant de pouvoir déclencher le passage au niveau 24. [[1](https://www.youtube.com/watch?v=5i-Nyacw4go\&t=537), [2](https://www.youtube.com/watch?v=_QSsOBihZb0\&t=36)]

**2. Achat individuel des segments avec de l'or**

- **Paiement segment par segment.** Vous n'avez pas besoin d'économiser la totalité du coût d'un niveau en une seule fois : vous achetez chaque segment individuellement dès que vous disposez de la somme d'or requise. [[1](https://www.youtube.com/watch?v=_QSsOBihZb0\&t=36), [2](https://guidesbygrace.uk/gear-lamp)]
- **Progression enregistrée.** Chaque clic remplit une fraction de la jauge d'amélioration de la lampe et retire immédiatement l'or correspondant de votre réserve.

**3. Déclenchement du temps de construction**

- **Démarrage uniquement à 100 %.** Le minuteur de construction ne se lance qu'une fois **tous les segments du niveau…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T082`.


#### T083 · SYS-002.D.11.1.5.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T083`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t083) — export ligne 27188; réponse ligne 27193.

**Prescription approuvée :** C'est le modèle A

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Fin du minuteur | `automatic` |
| Validation manuelle | `not_required` |
| Augmentation du niveau | `automatic` |
| Déblocage des segments suivants | `immediate` |
| Utilisation de la lampe pendant construction | `allowed` |


#### T084 · SYS-002.D.11.1.6

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T084`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t084) — export ligne 27262; réponse ligne 27289.

**Prescription approuvée (début) :** **Dans *Legend of Mushroom*, le minuteur de la lampe suit une progression exponentielle allant de quelques secondes à plusieurs jours, que vous pouvez réduire grâce aux tickets d'accélération (5 minutes chacun), aux publicités quotidiennes et à l'aide de votre clan.**

**1. Évolution de la durée de construction**

- **Début de partie (Niveaux 1 à 10).** Les premiers délais sont très courts, passant de quelques secondes à quelques dizaines de minutes.
- **Milieu de partie (Niveaux 11 à 20).** La durée grimpe progressivement de plusieurs heures à plus d'une journée complète par palier.
- **Haut niveau (Niveaux 21 à 28+).** Le minuteur devient un véritable goulot d'étranglement, atteignant **plusieurs jours complets** à partir du niveau 24 (nécessitant plus de 1 200 tickets d'accélération pour être passé instantanément, comme le soulignent les joueurs sur [**Reddit Legend of Mushroom**](https://www.reddit.com/r/LegendOfMushroomGame/comments/1crdw6g/had_the_game_a_couple_weeks_and_im_just_realizing/)).

**2. Tickets d'accélération (*Speed-Up Coupons*)**

- **Valeur unitaire fixe.** Chaque ticket d'accélération standard retire exactement **5 minutes** au compte à rebours en cours.
- **Cumul illimité.** Les tickets sont entièrement cumulables : un bouton dédié sur la fenêtre du minuteur permet d'utiliser d'un seul coup le nombre exact de tickets nécessaires pour terminer l'amélioration (ou de vider votre stock).
- **Double usage.** Comme le rappelle [**Pocket Gamer**](https://www.pocketgamer.com/legend-of-mushroom/guide/), ces mêmes tickets servent également à accélérer les…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T084`.

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Valeur unitaire | 5 minutes |
| Cumul | Additif |
| Utilisation multiple | Autorisée |
| Utilisation partielle | Autorisée |
| Dépense maximale | Stock disponible |
| Utilisation dans d'autres systèmes | Recherche technologique |
| Débit | Immédiat et atomique |


#### T085 · SYS-002.D.11.1.6.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T085`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t085) — export ligne 27560; réponse ligne 27565.

**Prescription approuvée :** Je valide le modèle A

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Source temporelle | `local_utc` |
| Écoulement hors ligne | `continuous` |
| Persistance | `absolute_timestamp` |
| Reprise | `automatic_reconciliation` |
| Finalisation | `automatic` |
| Dépendance serveur | `none` |
| Tolérance aux changements d'horloge | `known_limitation` |


#### T086 · SYS-002.D.11.1.7

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T086`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t086) — export ligne 27646; réponse ligne 27673.

**Prescription approuvée (début) :** **L'aide de la Famille (Clan) fonctionne par requête unique par amélioration en cours, permettant à vos alliés de réduire gratuitement votre minuteur de construction ou de recherche technologique tout en gagnant des points de contribution**.

Voici le fonctionnement exact de chacun des quatre points dans *Legend of Mushroom* :

**1. Limite par membre (Une aide par allié)**

- **Une seule contribution par membre et par requête.** Chaque membre de votre Famille ne peut cliquer qu'une seule fois sur votre demande d'assistance dans l'onglet d'aide du clan.
- **Récompense pour l'aidant.** Comme expliqué dans les guides sur le système familial sur [**YouTube**](https://www.youtube.com/watch?v=O618QuvVAmw), chaque allié qui clique sur « Aider » reçoit en retour des **points de contribution familiale** (utilisables dans la boutique de famille, soumise à un plafond quotidien de gains d'aide).

**2. Durée retirée par assistance**

- **Réduction fixe (ou pourcentage encadré) par clic.** Chaque aide validée par un membre retire immédiatement une portion fixe du temps restant sur le minuteur (généralement **1 % du temps total de construction avec un minimum fixe de quelques minutes** selon le niveau du bâtiment/lampe).
- **Impact concret sur les longs minuteurs.** Sur les améliorations de lampe dépassant 24 à 72 heures, cumuler l'ensemble des aides de votre famille permet d'économiser plusieurs heures complètes sans dépenser de tickets d'accélération.

**3. Nombre maximal d'assistances par niveau**

- **Plafond lié au niveau de la Famille.** Il existe bien un **nombre maximal d'aides…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T086`.

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Règle |
|--------|--------|
| Demandes par construction | 1 |
| Aides par membre et par demande | 1 |
| Nombre maximal d'aides | Dépend du niveau du clan |
| Renouvellement de demande | Interdit |
| Changement de clan | Ne réinitialise pas la demande |
| Expiration | Automatique lorsque le minuteur atteint zéro |


#### T087 · SYS-002.D.11.1.7.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T087`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t087) — export ligne 27882; réponse ligne 27887.

**Prescription approuvée :** Validation SYS-002.D.11.1.7.1 : modèle = simulation

**Tableau de formalisation consécutive à la validation :**

| ID | Paramètre | Décision |
|--------|--------|--------|
| CLAN-SIM-001 | Mode | `local_simulation` |
| CLAN-SIM-002 | Membres | `virtual_members` |
| CLAN-SIM-003 | Niveau de Famille | `configurable` |
| CLAN-SIM-004 | Plafond d'assistance | `family_level_lookup` |
| CLAN-SIM-005 | Aide par membre | `once_per_request` |
| CLAN-SIM-006 | Demandes | `one_per_construction` |
| CLAN-SIM-007 | Changement de clan | `no_reset` |
| CLAN-SIM-008 | Récompenses | `virtual_member_contribution` |
| CLAN-SIM-009 | Plafond quotidien | `per_member` |
| CLAN-SIM-010 | Expiration | `automatic` |


#### T088 · SYS-002.D.11

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T088`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t088) — export ligne 28058; réponse ligne 28097.

**Prescription approuvée (début) :** Je choisis le modèle B.

Je répond en détaillant la première question :
Dans Legend of Mushroom, la Lampe Magique génère aléatoirement des pièces pour 10 emplacements d'équipement standards répartis autour de votre personnage.

1. Les 10 emplacements générés par la Lampe Magique

Chaque tirage de lampe attribue l'objet à l'un des 10 emplacements suivants :
Colonne de gauche (Offensif et haut du corps)
• Arme (Weapon). Détermine l'apparence visuelle de votre attaque en combat et apporte un fort bonus d'Attaque de base.
• Casque / Chapeau (Helmet / Hat). Protège la tête de votre champignon.
• Lunettes / Masque (Glasses / Mask). Accessoire facial offrant des statistiques de base et secondaires.
• Épaulières (Shoulderpads). Renforce la défense et les points de vie.
• Armure / T-shirt (Armor / T-shirt). Pièce principale du torse.
Colonne de droite (Défensif et bas du corps)
• Brassards / Protège-bras (Armpad). Protège les avant-bras.
• Gants (Gloves). Équipement des mains.
• Ceinture (Belt). Renforce la taille et les statistiques globales.
• Pantalon / Genouillères (Pants / Kneepads). Pièce d'armure des jambes.
• Chaussures / Bottes (Shoes / Boots). Complète l'ensemble de base.
(Note : Vous pouvez enregistrer plusieurs préréglages d'équipement directement sur la fiche de personnage afin d'alterner rapidement entre vos ensembles PvP et PvE sans avoir à retrier vos pièces).

2. Caractéristiques communes à ces 10 emplacements

• Statistiques de base identiques. Contrairement à d'autres RPG où l'arme ne donne que de l'attaque et l'armure que de la défense, chaque pièce des 10…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T088`.

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Simulation | `progressive` |
| Réponse des membres | `scheduled` |
| Délai de réponse | `member_profile` |
| Assistance par membre | `once_per_request` |
| Nombre maximal | `family_level_lookup` |
| Récompenses | `contribution_points` |
| Fonctionnement hors ligne | `local_utc` |
| Persistance des réponses | `persistent` |
| Changement de clan | `no_reset` |


#### T089 · SYS-002.D.11.1.10

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T089`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t089) — export ligne 28460; réponse ligne 28488.

**Prescription approuvée (début) :** Dans *Legend of Mushroom*, **le nombre d'affixes (statistiques secondaires soulignées) plafonne très rapidement à 2 maximum sur l'ensemble des équipements de la Lampe Magique**. [[1](https://www.allclash.com/best-setup-for-mage-class-mushroom-in-legend-of-mushroom/)]

Contrairement à d'autres RPG où les raretés ultimes empilent 4 ou 5 lignes bonus, les 10 raretés de *Legend of Mushroom* plafonnent dès le palier *Bien* (*Well*) et font évoluer **la puissance des pourcentages** ainsi que **la probabilité d'obtenir ces affixes** plutôt que leur quantité.

**1. Nombre d'affixes par rareté (Paliers 1 à 10)**

| **Palier** | **Rareté (Jeu)**             | **Nombre d'affixes** | **Évolution des statistiques secondaires**                                                                     |
| ---------- | ---------------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------- |
| **1**      | **Normal** (*Normal*)        | **0 affixe**         | Uniquement les statistiques de base (PV, ATQ, DÉF).                                                            |
| **2**      | **Unique** (*Unique*)        | **0 à 1 affixe**     | Apparition occasionnelle d'une première statistique secondaire faible.                                         |
| **3**      | **Bien** (*Well*)            | **1 à 2 affixes**    | Plafond atteint : il est déjà possible de tirer 2 affixes sur une pièce verte.                                 |
| **4**      | **Rare** (*Rare*)            | **2 affixes**        | Deux…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T089`.


#### T090 · SYS-002.D.11.1.10.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T090`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t090) — export ligne 28706; réponse ligne 28711.

**Prescription approuvée :** SYS-002.D.11.1.10.5 — Validation : unicité des affixes = distinct

**Tableau de formalisation consécutive à la validation :**

| Règle | Décision |
|--------|--------|
| Doublons d'affixes sur une pièce | Interdits |
| Sélection de deux affixes | Sans remise |
| Valeurs numériques | Générées individuellement |
| Même affixe sur plusieurs pièces | Autorisé |
| Nombre maximal | 2 |
| Unicité | Par équipement |


#### T092 · SYS-002.D.11.1.10.7

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T092`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t092) — export ligne 28927; réponse ligne 28950.

**Prescription approuvée (début) :** **Dans *Legend of Mushroom*, la probabilité d'apparition des affixes secondaires suit une distribution uniforme (équiprobable) à l'intérieur du bassin d'affixes actifs, et c'est uniquement la mécanique de bannissement qui modifie ces chances en augmentant le niveau de la Lampe Magique.**

Contrairement aux raretés d'équipement dont les taux exacts sont affichés en jeu, le jeu ne favorise pas un attribut secondaire par rapport à un autre lors d'un tirage standard. [[1](https://www.youtube.com/watch?v=3HAAYhYqQlw), [2](https://theriagames.com/guide/legend-of-mushroom-beginner-guide/)]

**1. Équiprobabilité des affixes standards**

- **Aucune pondération cachée.** Lorsqu'une pièce d'équipement génère ses deux statistiques secondaires (Combo, Coup Critique, Contre-attaque, Étourdissement, Coup critique de compétence, Combo d'Acolyte, Coup critique d'acolyte,  Régénération, Evasion), chaque statistique disponible dans le pool possède la même probabilité de sortir.
- **Biais de perception des joueurs.** L'impression de tirer plus souvent des statistiques inutiles vient simplement du fait que sur 9 statistiques possibles, seule une combinaison précise de **2 affixes** correspond parfaitement à votre classe (par exemple *Critique + Combo* pour Archer ou *Critique + Contre-attaque* pour Guerrier).
- **Indépendance des tirages.** Comme le confirme la communauté sur [**Reddit**](https://www.reddit.com/r/LegendofMushroom/comments/1e6whkx/lamps_chances_of_rarity/), ouvrir les lampes une par une ou par lots en mode automatique applique exactement les mêmes tirages aléatoires sans aucune…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T092`.

**Tableau de formalisation consécutive à la validation :**

| ID | Règle |
|--------|--------|
| AFFIX-PROB-001 | Pool global commun aux dix emplacements |
| AFFIX-PROB-002 | Neuf affixes standards dans la configuration initiale |
| AFFIX-PROB-003 | Probabilité uniforme |
| AFFIX-PROB-004 | Sélection sans remise |
| AFFIX-PROB-005 | Adjust appliqué avant sélection |
| AFFIX-PROB-006 | Aucune compensation par pondération |
| AFFIX-PROB-007 | Nombre d'affixes défini par la rareté |
| AFFIX-PROB-008 | Tirages indépendants entre équipements |
| AFFIX-PROB-009 | Tirages multiples sans pénalité |
| AFFIX-PROB-010 | Générateur aléatoire injectable |


#### T093 · SYS-002.D.11.1.10.8

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T093`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t093) — export ligne 29178; réponse ligne 29183.

**Prescription approuvée :** Validation SYS-002.D.11.1.10.8 : conditions Aurous/Eternel = unlock_only

**Tableau de formalisation consécutive à la validation :**

| ID | Règle | Décision |
|--------|--------|--------|
| RAR-001 | Déblocage des raretés avancées | Conditionnel |
| RAR-002 | Conditions de déblocage | Configurables |
| RAR-003 | Affixe de classe obligatoire | Non |
| RAR-004 | Pool d'affixes | Universel |
| RAR-005 | Distribution des affixes | Uniforme |
| RAR-006 | Doublons d'affixes | Interdits |
| RAR-007 | Exclusions Adjust | Appliquées normalement |
| RAR-008 | Génération hors conditions | Interdite |


#### T094 · SYS-002.D.11.1.11.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T094`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t094) — export ligne 29446; réponse ligne 29451.

**Prescription approuvée :** Validation SYS-002.D.11.1.11.1 : distribution des raretés verrouillées = normalized


#### T095 · SYS-002.D.11.1.11.2

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T095`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t095) — export ligne 29672; réponse ligne 29685.

**Prescription approuvée (début) :** **Oui, chacun des 10 emplacements d'équipement dispose d'une probabilité uniforme de 10 % (1 chance sur 10) lors d'un tirage de la Lampe Magique.**

Contrairement aux raretés dont les pourcentages sont pondérés et affichés dans le tableau de la lampe, la sélection de l'emplacement obéit à un tirage aléatoire pur et équitable :

**1. Distribution uniforme entre les 10 emplacements**

- **Équiprobabilité parfaite (10 %).** Lorsqu'une charge de lampe génère un objet, le jeu tire d'abord la rareté selon la table de probabilités de votre niveau de lampe, puis sélectionne l'un des **10 emplacements** (Arme, Casque, Lunettes, Épaulières, Armure, Brassards, Gants, Ceinture, Pantalon, Chaussures) avec une probabilité identique de **10 %** chacun. [[1](https://www.deconstructoroffun.com/blog/2024/4/15/the-magic-of-legend-of-mushroom), [2](https://www.youtube.com/watch?v=3HAAYhYqQlw\&t=29)]
- **Aucune pondération par pièce.** L'arme n'est pas plus rare que les bottes ou la ceinture, et le niveau de la lampe ne modifie jamais la répartition entre les emplacements.
- **Indépendance des tirages.** Comme le confirment les analyses de fonctionnement de la lampe sur [**Deconstructor of Fun**](https://www.deconstructoroffun.com/blog/2024/4/15/the-magic-of-legend-of-mushroom) et les retours de la communauté sur [**Reddit Legend of Mushroom**](https://www.reddit.com/r/LegendofMushroom/comments/1e6whkx/lamps_chances_of_rarity/), chaque tirage est totalement indépendant du précédent, qu'il soit effectué manuellement ou par lots via le mode automatique.…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T095`.

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Nombre d'emplacements | 10 |
| Distribution | `uniform` |
| Probabilité individuelle | 10 % |
| Influence du niveau de lampe | `none` |
| Influence de la rareté | `none` |
| Influence du niveau personnage | `none` |
| Dépendance entre tirages | `independent` |
| Tirages groupés | `sequential_independent` |
| Système de garantie | `none` |
| Ordre de sélection | `rarity_then_slot` |


#### T096 · SYS-002.D.11.1.12.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T096`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t096) — export ligne 29868; réponse ligne 29873.

**Prescription approuvée :** Validation SYS-002.D.11.1.12.1 : génération des statistiques de base = random_range

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Génération | `random_range` |
| Statistiques concernées | `hp`, `attack`, `defense` |
| Dépendance au niveau personnage | `enabled` |
| Dépendance à la rareté | `enabled` |
| Dépendance à l'emplacement | `configurable` |
| Bornes numériques | `configurable_lookup` |
| Génération individuelle | `per_equipment` |
| RNG | `injectable_rng` |
| Reproductibilité | `seeded_generation` |
| Fourneau Magique | `separate_calculation` |


#### T097 · SYS-002.D.11.1.12.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T097`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t097) — export ligne 30047; réponse ligne 30052.

**Prescription approuvée :** Modèle A

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Génération PV | `independent_draw` |
| Génération ATQ | `independent_draw` |
| Génération DÉF | `independent_draw` |
| Facteur de qualité commun | `none` |
| Corrélation imposée | `none` |
| Plages numériques | `per_stat` |
| Distribution individuelle | `pending` |
| RNG | `injectable_rng` |
| Reproductibilité | `seeded_generation` |


#### T098 · SYS-002.D.11.1.12.3

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T098`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t098) — export ligne 30213; réponse ligne 30218.

**Prescription approuvée :** c'est une distribution uniforme

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Distribution PV | `uniform` |
| Distribution ATQ | `uniform` |
| Distribution DÉF | `uniform` |
| Tirages | `independent` |
| Bornes | `inclusive` |
| Pondération | `none` |
| Facteur de qualité | `none` |
| RNG | `injectable_rng` |


#### T099 · SYS-002.D.11.1.12.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T099`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t099) — export ligne 30319; réponse ligne 30338.

**Prescription approuvée (début) :** Modèle A.

Précisions :

**Les valeurs plates de PV, ATQ et DÉF affichées sur les équipements dans *Legend of Mushroom* sont toujours des nombres entiers.** Le jeu n'affiche jamais de décimales pour les statistiques de base plates, que ce soit sur la fiche de l'objet ou dans l'écran de comparaison de la Lampe Magique.

**1. Affichage en nombres entiers et grands nombres**

- **Arrondi à l'entier sur l'équipement.** Lors du calcul interne à partir du niveau d'objet, de la rareté et de l'emplacement, le jeu arrondit systématiquement le résultat pour afficher un **nombre entier exact** sur la carte de l'objet (ex. `ATQ +12 450`, `PV +98 200`, `DÉF +4 120`).
- **Notation abrégée à haut niveau.** Dès que les valeurs dépassent les dizaines de milliers ou les millions en milieu/fin de jeu, l'interface bascule sur des suffixes abrégés (**K** pour mille, **M** pour million, **B** pour milliard, **T** pour billion, puis AA, AB, etc.) avec deux décimales d'affichage (par exemple `14.52M` = `14 520 000`), mais la valeur brute sous-jacente reste un entier.

**2. Distinction avec les statistiques en pourcentage**

- **Les affixes et bonus utilisent des décimales.** Contrairement aux valeurs plates (PV, ATQ, DÉF), les **affixes secondaires** de l'équipement (ex. `Combo +3.45 %`, `Critique +2.8 %`) ainsi que les bonus passifs des acolytes, reliques ou statues comportent régulièrement **1 à 2 décimales**.
- **Calcul en combat.** Lors de l'application des multiplicateurs en pourcentage sur les statistiques entières de base, le moteur de combat effectue les calculs en virgule flottante avant…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T099`.

**Tableau de formalisation consécutive à la validation :**

| ID | Règle |
|--------|--------|
| BASE-NUM-001 | Les PV, ATQ et DÉF sont des entiers |
| BASE-NUM-002 | Les trois valeurs sont générées indépendamment |
| BASE-NUM-003 | Chaque tirage suit une distribution uniforme discrète |
| BASE-NUM-004 | Les bornes minimale et maximale sont incluses |
| BASE-NUM-005 | Les valeurs originales sont conservées sans perte |
| BASE-NUM-006 | La notation K/M/B/T n'affecte pas les calculs |
| BASE-NUM-007 | Les affixes sont représentés séparément des statistiques plates |
| BASE-NUM-008 | Le moteur de combat conserve la précision intermédiaire avant l'arrondi final |


#### T100 · SYS-002.D.11.1.12.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T100`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t100) — export ligne 30524; réponse ligne 30529.

**Prescription approuvée :** Validation SYS-002.D.11.1.12.5 : modèle de plages des statistiques par emplacement = same

**Tableau de formalisation consécutive à la validation :**

| ID | Paramètre | Décision |
|--------|--------|--------|
| BASE-SLOT-001 | Plages par emplacement | `shared` |
| BASE-SLOT-002 | Modificateurs propres aux emplacements | `none` |
| BASE-SLOT-003 | Dépendance au niveau personnage | `enabled` |
| BASE-SLOT-004 | Dépendance à la rareté | `enabled` |
| BASE-SLOT-005 | Génération | `uniform_discrete` |
| BASE-SLOT-006 | Corrélation PV / ATQ / DÉF | `independent` |
| BASE-SLOT-007 | Précision des statistiques | `integer` |
| BASE-SLOT-008 | Remplacement d'équipement | `no_reroll` |


#### T101 · SYS-002.D.11.1.12.6

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T101`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t101) — export ligne 30748; réponse ligne 30753.

**Prescription approuvée :** Validation SYS-002.D.11.1.12.6 : modèle de progression des plages statistiques = anchors


#### T102 · SYS-002.D.11.1.12.6.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T102`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t102) — export ligne 31040; réponse ligne 31045.

**Prescription approuvée :** Validation SYS-002.D.11.1.12.6.2 : coefficients de rareté = single

**Tableau de formalisation consécutive à la validation :**

| ID | Règle | Valeur |
|--------|--------|--------|
| RAR-SCALE-001 | Modèle | `single_multiplier` |
| RAR-SCALE-002 | Nombre de coefficients | 1 par rareté |
| RAR-SCALE-003 | Statistiques affectées | PV, ATQ, DÉF |
| RAR-SCALE-004 | Bornes affectées | Minimum et maximum |
| RAR-SCALE-005 | Dépendance à l'emplacement | Aucune |
| RAR-SCALE-006 | Dépendance au niveau de lampe | Aucune |
| RAR-SCALE-007 | Application | Avant le tirage uniforme |


#### T103 · SYS-002.D.11.1.12.6.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T103`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t103) — export ligne 31372; réponse ligne 31377.

**Prescription approuvée :** Validation SYS-002.D.11.1.12.6.4 : quantification des bornes = inward. Formalise cette décision dans le GDD, puis soumets les contraintes de croissance à validation avant de commencer la calibration numérique

**Tableau de formalisation consécutive à la validation :**

| ID | Règle | Statut |
|--------|--------|--------|
| QUANT-001 | Quantification intérieure | (Validé) |
| QUANT-002 | Plafond pour la borne minimale | (Validé) |
| QUANT-003 | Plancher pour la borne maximale | (Validé) |
| QUANT-004 | Quantification après interpolation et multiplication | (Validé) |
| QUANT-005 | Tirage uniforme entier inclusif | (Validé) |
| QUANT-006 | Plage entière vide rejetée | (Validé) |
| QUANT-007 | Intermédiaires calculés avec précision exacte | (Validé) |


#### T104 · SYS-002.D.11.1.12.6.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T104`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t104) — export ligne 31614; réponse ligne 31619.

**Prescription approuvée :** Validation SYS-002.D.11.1.12.6.3 : contraintes de croissance = strict

**Tableau de formalisation consécutive à la validation :**

| ID | Paramètre | Décision |
|--------|--------|--------|
| GROWTH-001 | Croissance selon le niveau personnage | Non décroissante |
| GROWTH-002 | Croissance selon la rareté | Non décroissante |
| GROWTH-003 | Coefficient Normal | Exactement `1` |
| GROWTH-004 | Coefficients de rareté | Strictement positifs |
| GROWTH-005 | Paliers de progression | Autorisés |
| GROWTH-006 | Régressions | Rejet de configuration |
| GROWTH-007 | Validation | Au chargement de la configuration |
| GROWTH-008 | Correction automatique de données invalides | Interdite |


#### T105 · SYS-002.D.11.1.12.7.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T105`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t105) — export ligne 31898; réponse ligne 31903.

**Prescription approuvée :** Validation SYS-002.D.11.1.12.7.2 : stratégie de calibration = provisional

**Tableau de formalisation consécutive à la validation :**

| ID | Paramètre | Décision |
|--------|--------|--------|
| CAL-STRAT-001 | Stratégie | `provisional` |
| CAL-STRAT-002 | Profil actif initial | `equipment_base_stats_v0.1` |
| CAL-STRAT-003 | Provenance | `designed` |
| CAL-STRAT-004 | Niveaux couverts | 1-200 |
| CAL-STRAT-005 | Raretés couvertes | 10 |
| CAL-STRAT-006 | Interpolation | Linéaire entre ancrages |
| CAL-STRAT-007 | Coefficients de rareté | Un multiplicateur commun aux trois statistiques |
| CAL-STRAT-008 | Contraintes de croissance | Strictes |
| CAL-STRAT-009 | Quantification | Intérieure |
| CAL-STRAT-010 | Remplacement du profil | Par version de configuration |
| CAL-STRAT-011 | Modification rétroactive des objets | Interdite |


#### T106 · SYS-002.D.11.1.13.2

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T106`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t106) — export ligne 32248; réponse ligne 32253.

**Prescription approuvée :** Validation SYS-002.D.11.1.13.2 : dépendance des valeurs d'affixes = rarity_only


#### T107 · SYS-002.D.11.1.13.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T107`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t107) — export ligne 32649; réponse ligne 32654.

**Prescription approuvée :** Validation SYS-002.D.11.1.13.3 : distribution numérique des affixes = uniform

**Tableau de formalisation consécutive à la validation :**

| ID | Paramètre | Valeur |
|--------|--------|--------|
| AFFIX-DIST-001 | Distribution | `uniform_discrete` |
| AFFIX-DIST-002 | Unité | Basis points |
| AFFIX-DIST-003 | Précision | 0,01 % |
| AFFIX-DIST-004 | Pas numérique | 1 BP |
| AFFIX-DIST-005 | Bornes | Inclusives |
| AFFIX-DIST-006 | Dépendance | Rareté + type |
| AFFIX-DIST-007 | Niveau personnage | Sans influence |
| AFFIX-DIST-008 | Tirages successifs | Indépendants |


#### T108 · SYS-002.D.11.1.13.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T108`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t108) — export ligne 33054; réponse ligne 33059.

**Prescription approuvée :** Je valide

**Tableau de formalisation consécutive à la validation :**

| ID | Règle | Décision |
|--------|--------|--------|
| AFFIX-GROW-001 | Minimum non décroissant | Validé |
| AFFIX-GROW-002 | Maximum non décroissant | Validé |
| AFFIX-GROW-003 | Valeurs strictement positives | Validé |
| AFFIX-GROW-004 | Minimum inférieur ou égal au maximum | Validé |
| AFFIX-GROW-005 | Pas numérique | 1 BP |
| AFFIX-GROW-006 | Alignement des bornes | Obligatoire |
| AFFIX-GROW-007 | Chevauchement des plages | Autorisé |
| AFFIX-GROW-008 | Croissance de la largeur | Libre |
| AFFIX-GROW-009 | Indépendance entre familles | Validée |
| AFFIX-GROW-010 | Profils indisponibles | Inactifs |


#### T109 · SYS-002.D.11.1.14.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T109`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t109) — export ligne 33318; réponse ligne 33323.

**Prescription approuvée :** Oui je valide

**Tableau de formalisation consécutive à la validation :**

| ID | Règle | Décision |
|--------|--------|--------|
| ADJUST-PERSIST-001 | Persistance | `persistent_global` |
| ADJUST-PERSIST-002 | Portée | Toutes les pièces générées par la Lampe |
| ADJUST-PERSIST-003 | Durée | Jusqu'à modification |
| ADJUST-PERSIST-004 | Conservation hors ligne | Obligatoire |
| ADJUST-PERSIST-005 | Modification de la liste | Immédiatement enregistrée |
| ADJUST-PERSIST-006 | Application | Prochaine génération |
| ADJUST-PERSIST-007 | Modification rétroactive | Interdite |
| ADJUST-PERSIST-008 | Ouverture groupée | Configuration figée au démarrage |
| ADJUST-PERSIST-009 | Historique | Version de configuration conservée |


#### T110 · SYS-002.D.11.1.15.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T110`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t110) — export ligne 33614; réponse ligne 33619.

**Prescription approuvée :** Validation SYS-002.D.11.1.15.1 : distribution du nombre d'affixes = weighted_lookup


#### T111 · SYS-002.D.11.1.17.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T111`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t111) — export ligne 34136; réponse ligne 34141.

**Prescription approuvée :** Validation SYS-002.D.11.1.17.1 : architecture de configuration Unity = hybrid


### 12 - Classes, spécialisations et passifs

#### T113 · SYS-002.D.12.1

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T113`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t113) — export ligne 35560; réponse ligne 35565.

**Prescription approuvée :** Je souhaite rester assez fidèle avec l'originale mais tout en nous laissant libre de modifier certaines mécaniques si nécessaire ou plus cohérent


#### T114 · SYS-002.D.12.2

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T114`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t114) — export ligne 35768; réponse ligne 35837.

**Prescription approuvée (début) :** Je n'ai pas de capture d'écran, le rendu est pas assez clair et compréhensible.

Je vais faire un listing des différentes informations :

Dans *Legend of Mushroom*, **tous les joueurs débutent en tant que Champignon (*Shroomie*) au niveau 1, évoluent en Aventurier (*Adventurer*) au niveau 15, puis choisissent au niveau 30 l'une des 4 classes principales** (Combattant/Guerrier, Archer, Mage ou Dompteur/Channeler), chacune se divisant en deux branches spécialisées au niveau 50 jusqu'à l'**Éveil** (et la Transcendance en très haut niveau). [[1](https://www.bluestacks.com/blog/game-guides/legend-of-the-mushroom-brave-3000-free-draws/lotmb-classes-guide-en.html), [2](https://mobi.gg/en/tips/legend-of-mushroom-class/), [3](https://www.youtube.com/watch?v=NagLq0be1SY\&t=1)]

Voici l'arbre complet des classes et de leurs évolutions successives (Niveaux 30 → 50 → 70 → 100 → Éveil) : [[1](https://www.bluestacks.com/blog/game-guides/legend-of-the-mushroom-brave-3000-free-draws/lotmb-classes-guide-en.html)]

**1. Branche Combattant / Guerrier (*Warrior*) — Mêlée, PV et Contre-attaque**

- **Niveau 30 :** Combattant / Guerrier (*Warrior*) [[1](https://www.bluestacks.com/blog/game-guides/legend-of-the-mushroom-brave-3000-free-draws/lotmb-classes-guide-en.html), [2](https://mobi.gg/fr/astuces/classes-legend-of-mushroom/)]
- **Branche A (Défense, boucliers et résistance) :**
  - **Niveau 50 :** Épéiste (*Swordsman*)
  - **Niveau 70 :** Porteur de Claymore / Grand Maître de l'Épée (*Claymore Wielder*)
  - **Niveau 100 :** Maître d'armes / Tête de l'Épée (*Swordmaster*)
  - **Éveil :**…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T114`.


#### T115 · SYS-002.D.12.3

**Autorité :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Traçabilité :** [`T115`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t115) — export ligne 36209; réponse ligne 36249.

**Prescription approuvée (début) :** Dans *Legend of Mushroom*, **la branche Guerrier (*Warrior*) repose sur une compétence active de classe évolutive (qui inflige des dégâts de zone et amplifie la contre-attaque sur les ennemis touchés) ainsi que sur l'empilement progressif de 5 compétences passives aux paliers 30, 50, 70 et 100, culminant avec l'Éveil**.

---

**1. Évolution de la Compétence Active de Classe**

Contrairement aux 5 emplacements de compétences invocables au gacha, la compétence active propre à votre classe s'améliore automatiquement à chaque promotion :

- **Niveau 30 (Combattant / Guerrier) :** Inflige des dégâts physiques de zone (AoE) devant vous et augmente légèrement les dégâts subis par les cibles.
- **Niveaux 50, 70 et 100 (Épéiste → Maître d'armes / Guerrier à la hache → Belliciste) :** Le multiplicateur de dégâts de zone augmente à chaque palier, et la compétence applique un débuff de **5 secondes** qui augmente les **dégâts de contre-attaque subis par les ennemis à portée de +60 %** (ou réduit leur résistance aux dégâts de contre-attaque de 40 % selon les équilibrages de patch), comme détaillé sur [**BlueStacks**](https://www.bluestacks.com/fr/blog/game-guides/legend-of-the-mushroom-brave-3000-free-draws/lotmb-classes-guide-fr.html).
- **Éveil – Branche Tank (*Saint Martial / Martial Sage*) :** La durée du débuff de contre-attaque passe de 5 à **8 secondes**, chaque contre-attaque inflige des dégâts bonus basés sur les PV actuels de la cible, et vous régénérez continuellement **15 % de vos PV max pendant 5 secondes**.
- **Éveil – Branche DPS (*Porteur de guerre / Warbringer*) :** La…

**Texte intégral de cette prescription :** annexe des décisions propriétaire, `T115`.


#### T116 · SYS-002.D.12.3.4

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T116`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t116) — export ligne 36725; réponse ligne 36730.

**Prescription approuvée :** Validation SYS-002.D.12.3.4 : modèle de débuff Guerrier = configurable

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Décision |
|--------|--------|
| Mode | `configurable` |
| Mode initial | `COUNTER_DAMAGE_TAKEN_MULTIPLIER` |
| Valeur initiale | \+60 % |
| Mode alternatif | `COUNTER_RESISTANCE_REDUCTION` |
| Valeur alternative | -40 points de pourcentage |
| Durée standard | 5 secondes |
| Durée après Éveil | 8 secondes |
| Cibles | Ennemis touchés par la compétence de zone |
| Application | Via le Modifier Engine |
| Empilement | Régi par une politique explicite |
| Changement de mode | Par version de configuration |


#### T117 · SYS-002.D.12.3.7

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T117`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t117) — export ligne 37206; réponse ligne 37211.

**Prescription approuvée :** Validation SYS-002.D.12.3.7 : profil des passifs Guerrier = patch_reference

**Tableau de formalisation consécutive à la validation :**

| ID | Décision |
|--------|--------|
| `WAR-PASS-001` | Cinq passifs standards par lignée |
| `WAR-PASS-002` | P1 et P2 communs aux deux branches |
| `WAR-PASS-003` | P3, P4 et P5 propres à la spécialisation |
| `WAR-PASS-004` | Les passifs antérieurs restent actifs après promotion |
| `WAR-PASS-005` | Aucun cumul entre anciennes et nouvelles versions d'un même passif |
| `WAR-PASS-006` | Les passifs d'Ascension restent hors de ce référentiel |
| `WAR-PASS-007` | Chaque valeur numérique est modifiable par configuration versionnée |


#### T118 · SYS-002.D.12.3.11.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T118`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t118) — export ligne 37697; réponse ligne 37702.

**Prescription approuvée :** Validation SYS-002.D.12.3.11.1 : profils d'Éveil Guerrier = configurable

**Tableau de formalisation consécutive à la validation :**

| ID | Règle | Décision |
|--------|--------|--------|
| AWK-PROFILE-001 | Architecture | `configurable_profiles` |
| AWK-PROFILE-002 | Profil initial | `PATCH_REFERENCE` |
| AWK-PROFILE-003 | Profil alternatif | `LEGACY` |
| AWK-PROFILE-004 | Cumul entre profils | Interdit |
| AWK-PROFILE-005 | Sélection | Par version de configuration |
| AWK-PROFILE-006 | État durant le combat | Snapshot immuable |
| AWK-PROFILE-007 | Évolution du personnage | Une seule spécialisation active |
| AWK-PROFILE-008 | Compatibilité | Combat Engine et Modifier Engine existants |


#### T119 · SYS-002.D.12.3.15.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T119`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t119) — export ligne 38070; réponse ligne 38075.

**Prescription approuvée :** Validation SYS-002.D.12.3.15.1 : ciblage du bonus de vitesse d'attaque Warbringer = configurable

**Tableau de formalisation consécutive à la validation :**

| ID | Paramètre | Décision |
|--------|--------|--------|
| `WAR-TARGET-001` | Architecture | `configurable_target_selector` |
| `WAR-TARGET-002` | Ciblage initial | `HIT_ENEMIES` |
| `WAR-TARGET-003` | Variante | `ALLIES_IN_RANGE` |
| `WAR-TARGET-004` | Bonus de vitesse d'attaque | \+30 % |
| `WAR-TARGET-005` | Durée | 8 secondes |
| `WAR-TARGET-006` | Bonus de Défense | \+50 % sur Warbringer |
| `WAR-TARGET-007` | Sélection du profil | Au démarrage du combat |
| `WAR-TARGET-008` | Cumul entre variantes | Interdit |


#### T120 · SYS-002.D.12.3.15.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T120`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t120) — export ligne 38375; réponse ligne 38380.

**Prescription approuvée :** Validation SYS-002.D.12.3.15.5 : déclenchement réflexion = hit ; rafraîchissement = unique ; premières échéances périodiques = delayed. Formalise les trois décisions dans le GDD et poursuis l'audit des mécaniques Guerrier restantes, notamment la catégorisation des dégâts réfléchis, leur valeur de référence et les dégâts proportionnels aux PV de Martial Sage

**Tableau de formalisation consécutive à la validation :**

| ID | Mécanique | Décision |
|--------|--------|--------|
| `WAR-REF-001` | Déclenchement du renvoi | `ON_ELIGIBLE_BASIC_ATTACK_HIT` |
| `WAR-STACK-001` | Rafraîchissement des effets | `UNIQUE_SOURCE_REFRESH` |
| `WAR-TIME-001` | Première activation périodique | `DELAYED_FIRST_TICK` |


#### T121 · SYS-002.D.12.3.19.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T121`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t121) — export ligne 38913; réponse ligne 38918.

**Prescription approuvée :** Validation SYS-002.D.12.3.19.1 : catégorie des dégâts réfléchis = versioned

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Valeur |
|--------|--------|
| ATQ effective | 1 000 |
| Coefficient d'attaque normale | 150 % |
| Bonus de dégâts d'attaque normale | \+20 % |
| Coefficient de réflexion | 60 % |
| Bonus de dégâts de contre-attaque | \+140 % |


#### T122 · SYS-002.D.12.3.19.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T122`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t122) — export ligne 39446; réponse ligne 39451.

**Prescription approuvée :** Validation SYS-002.D.12.3.19.5 : contrat de résolution des dégâts Guerrier = proposed

**Tableau de formalisation consécutive à la validation :**

| ID | Mécanique | Contrat validé |
|--------|--------|--------|
| `WAR-DMG-009` | Référence du renvoi Warbringer | `CURRENT_BASIC_ATTACK_DAMAGE_PRE_TARGET` |
| `WAR-DMG-010` | Moment du calcul | Après la résolution du coup reçu et la mise à jour des statistiques réactives |
| `WAR-DMG-011` | Coefficient du renvoi | 60 % |
| `WAR-AOE-001` | Géométrie du renvoi | Zone centrée sur l'attaquant ayant déclenché le passif |
| `WAR-AOE-002` | Résolution des cibles | Base offensive commune, mitigation indépendante |
| `MS-DMG-001` | Bonus Martial Sage | 1 % des PV actuels de la cible avant impact |
| `MS-DMG-002` | Défense et résistances | Applicables |
| `MS-DMG-003` | Boucliers et immunité | Respectés |
| `MS-DMG-004` | Critique indépendant | Interdit |
| `MS-DMG-005` | Multiplicateurs offensifs supplémentaires | Non réappliqués |
| `MS-DMG-006` | Plafond particulier contre les boss | Aucun dans le profil initial |


#### T123 · SYS-002.D.12.3.24.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T123`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t123) — export ligne 39902; réponse ligne 39907.

**Prescription approuvée :** Validation SYS-002.D.12.3.24.1 : stratégie de calibration Guerrier = provisional

**Tableau de formalisation consécutive à la validation :**

| ID | Paramètre | Valeur |
|--------|--------|--------|
| `WAR-CAL-001` | Rayon du renvoi Warbringer | 2 unités logiques |
| `WAR-CAL-002` | Maximum de cibles du renvoi | 5 |
| `WAR-CAL-003` | Centre du renvoi | Position de l'attaquant déclencheur |
| `WAR-CAL-004` | Rayon de la compétence active | 3 unités logiques |
| `WAR-CAL-005` | Limite de cibles de la compétence | Toutes les cibles éligibles dans la zone |
| `WAR-CAL-006` | Cooldown de compétence | 12 secondes |
| `WAR-CAL-007` | Disponibilité initiale | Début du combat |
| `WAR-CAL-008` | Délai activation → impact | 250 millisecondes |
| `WAR-CAL-009` | Coefficients de dégâts par évolution | Calibration séparée |


#### T124 · SYS-002.D.12.3

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T124`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t124) — export ligne 40298; réponse ligne 40303.

**Prescription approuvée :** Je valide

**Tableau de formalisation consécutive à la validation :**

| ID | Mécanique | Contrat validé |
|--------|--------|--------|
| `WAR-ACT-009` | Acquisition des cibles | Utilisation du sélecteur principal du Combat Engine |
| `WAR-ACT-010` | Résolution de l'AoE | Détermination des cibles à l'impact |
| `WAR-ACT-011` | Délai d'impact provisoire | 250 ms après activation |
| `WAR-ACT-012` | Cible principale disparue | Dernière position capturée à l'activation |
| `WAR-REF-010` | Critique indépendant du renvoi | Interdit |
| `WAR-REF-011` | Combo déclenché par le renvoi | Interdit |
| `WAR-REF-012` | Nouveau jet d'esquive du renvoi | Interdit |
| `WAR-REF-013` | Réactions récursives | Interdites |
| `WAR-FATAL-001` | Réaction déclenchée par une frappe mortelle | Résolue avant la clôture du combat |
| `WAR-FATAL-002` | Double élimination | Transmise au moteur de rencontre |


#### T125 · SYS-002.D.12.4.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T125`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t125) — export ligne 40455; réponse ligne 40460.

**Prescription approuvée :** Oui je valide


#### T126 · SYS-002.D.12.4.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T126`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t126) — export ligne 40917; réponse ligne 40922.

**Prescription approuvée :** Validation SYS-002.D.12.4.5 : sémantique des passifs communs Archer = additive

**Tableau de formalisation consécutive à la validation :**

| ID | Passif | Valeur | Comportement validé |
|--------|--------|--------|--------|
| `ARCH-COM-001` | P1 - Combo Mastery | \+30 points de pourcentage | Contribution additive au taux de combo |
| `ARCH-COM-002` | P2 - Rapid Precision | \+15 % APS | Contribution au groupe de vitesse d'attaque |
| `ARCH-COM-003` | P2 - Rapid Precision | \+10 points de pourcentage | Réduction de l'évasion effective adverse |
| `ARCH-COM-004` | Disponibilité | Niveaux 30 et 40 | Passifs communs aux deux branches |
| `ARCH-COM-005` | Persistance | Aucun ajout permanent aux statistiques | Contributions reconstruites depuis la classe active |


#### T127 · SYS-002.D.12.4.12.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T127`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t127) — export ligne 41584; réponse ligne 41589.

**Prescription approuvée :** Validation SYS-002.D.12.4.12.1 : modèle multi-projectiles Archer = reference

**Tableau de formalisation consécutive à la validation :**

| ID | Règle | Décision |
|--------|--------|--------|
| `ARCH-PROJ-011` | Modèle retenu | `TOTAL_PROJECTILE_COUNT` |
| `ARCH-PROJ-012` | Niveau 30-50 | 1 projectile normal et 1 par combo |
| `ARCH-PROJ-013` | Niveau 70 | 1 projectile normal, 2 par combo |
| `ARCH-PROJ-014` | Niveau 100 et Éveil | 2 projectiles normaux, 2 par combo |
| `ARCH-PROJ-015` | Déclenchement du combo | Une fois par attaque parente éligible |
| `ARCH-PROJ-016` | Condition de combo | Au moins un projectile normal ayant touché |
| `ARCH-PROJ-017` | Esquive | Jet indépendant par projectile |
| `ARCH-PROJ-018` | Critique | Jet indépendant par projectile ayant touché |
| `ARCH-PROJ-019` | Combo récursif | Interdit |
| `ARCH-PROJ-020` | Nouveau cycle APS pour un projectile supplémentaire | Interdit |
| `ARCH-PROJ-021` | Redirection automatique sur une autre cible | Désactivée |
| `ARCH-PROJ-022` | Coefficients de dégâts | Configurables par type de projectile |


#### T128 · SYS-002.D.12.4.19.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T128`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t128) — export ligne 42268; réponse ligne 42273.

**Prescription approuvée :** Validation SYS-002.D.12.4.19.1 : coefficients des projectiles Archer = full

**Tableau de formalisation consécutive à la validation :**

| ID | Paramètre | Valeur validée |
|--------|--------|--------|
| `ARCH-DMG-001` | Modèle | `FULL_PER_PROJECTILE` |
| `ARCH-DMG-002` | Coefficient projectile normal | 100 % |
| `ARCH-DMG-003` | Coefficient projectile de combo | 100 % |
| `ARCH-DMG-004` | Représentation numérique | `10000 BP` par projectile |
| `ARCH-DMG-005` | Répartition des dégâts | Calcul indépendant par projectile |
| `ARCH-DMG-006` | Esquive | Un jet par projectile |
| `ARCH-DMG-007` | Critique | Un jet par projectile ayant touché |
| `ARCH-DMG-008` | Tirage de combo | Un maximum par action normale |
| `ARCH-DMG-009` | Bonus combo P3 | \+140 %, uniquement sur les dégâts de combo |
| `ARCH-DMG-010` | Provenance | `designed`, `approved_provisional` |


#### T129 · SYS-002.D.12.4.23.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T129`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t129) — export ligne 42824; réponse ligne 42829.

**Prescription approuvée :** Validation SYS-002.D.12.4.23.1 : compétences actives et Éveils Archer = reference

**Tableau de formalisation consécutive à la validation :**

| ID | Mécanique | Décision définitive |
|--------|--------|--------|
| `ARCH-ACT-001` | Compétence active | Compétence de classe automatique, indépendante du gacha |
| `ARCH-ACT-002` | Débuff initial | Réduction de résistance aux combos de 40 points |
| `ARCH-ACT-003` | Durée standard | 5 secondes |
| `ARCH-ACT-004` | Durée après Éveil | 8 secondes |
| `ARCH-ACT-005` | Application du débuff | Ennemis effectivement touchés |
| `ARCH-ACT-006` | Rafraîchissement | `UNIQUE_SOURCE_REFRESH` |
| `ARCH-SH-001` | Éveil Sacred Hunter | `SKILL_ENERGY_REGEN_SUPPRESSION` |
| `ARCH-SH-002` | Durée de suppression | 4 secondes |
| `ARCH-SH-003` | Énergie déjà accumulée | Conservée |
| `ARCH-SH-004` | Cooldowns indépendants | Non affectés |
| `ARCH-SH-005` | Régénération perdue pendant l'effet | Aucun rattrapage |
| `ARCH-PM-001` | Éveil Plume Monarch | `EVASION_CHECK_BYPASS` |
| `ARCH-PM-002` | Durée du bypass | 10 secondes |
| `ARCH-PM-003` | Attaques éligibles | Attaques normales et projectiles de combo du propriétaire |
| `ARCH-PM-004` | Acolytes | Non affectés |
| `ARCH-PM-005` | Boucliers, Défense et immunité | Toujours applicables |


#### T130 · SYS-002.D.12.4.29.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T130`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t130) — export ligne 43396; réponse ligne 43401.

**Prescription approuvée :** Validation SYS-002.D.12.4.29.1 : passifs Sacred Hunter = versioned. Formalise cette décision dans le GDD, puis finalise les règles temporelles et l'audit fonctionnel de l'Archer en vue de son passage à functionally_specified

**Tableau de formalisation consécutive à la validation :**

| ID | Mécanique | Décision |
|--------|--------|--------|
| `ARCH-SH-P3-001` | Architecture P3 | `versioned_profiles` |
| `ARCH-SH-P3-002` | Profil initial | `PATCH_REFERENCE` |
| `ARCH-SH-P3-003` | Profil historique | `LEGACY` |
| `ARCH-SH-P3-004` | Cumul entre profils | Interdit |
| `ARCH-SH-P3-005` | Activation | Branche critique à partir du niveau 50 |
| `ARCH-SH-P3-006` | Conservation après évolution | Oui |
| `ARCH-SH-P3-007` | Changement de profil | Par configuration versionnée |
| `ARCH-SH-P3-008` | Modification pendant un combat | Interdite |


#### T131 · SYS-002.D.12.4.34.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T131`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t131) — export ligne 44023; réponse ligne 44028.

**Prescription approuvée :** je valide

**Tableau de formalisation consécutive à la validation :**

| ID | Paramètre | Contrat |
|--------|--------|--------|
| `ARCH-FINAL-001` | Cooldown de compétence | 12 secondes, provisoire |
| `ARCH-FINAL-002` | Délai activation → impact | 250 ms, provisoire |
| `ARCH-FINAL-003` | Rayon AoE | 3 unités logiques, provisoire |
| `ARCH-FINAL-004` | Nombre de cibles | Toutes les cibles éligibles dans la zone |
| `ARCH-FINAL-005` | Ciblage | Cible principale ; sélection de zone à l'impact |
| `ARCH-FINAL-006` | Cible initiale disparue | Dernière position capturée à l'activation |
| `ARCH-FINAL-007` | Étourdissement après activation | N'annule pas l'impact déjà engagé |
| `ARCH-FINAL-008` | Mort du lanceur avant impact | Annule l'impact |
| `ARCH-FINAL-009` | Critique sous bouclier ou immunité | Déclenche P5 si l'impact et le critique sont confirmés |
| `ARCH-FINAL-010` | Expiration simultanée à un impact | Expiration prioritaire |
| `ARCH-FINAL-011` | Réapplication d'effet | `UNIQUE_SOURCE_REFRESH` |
| `ARCH-FINAL-012` | Coefficient AoE absent | Profil exécutable rejeté à la validation |


#### T132 · SYS-002.D.12.5.3

**Autorité :** `APPROBATION_CONTEXTUELLE` · **Traçabilité :** [`T132`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t132) — export ligne 44208; réponse ligne 44213.

**Prescription approuvée :** Oui


#### T133 · SYS-002.D.12.5.6.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T133`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t133) — export ligne 44559; réponse ligne 44564.

**Prescription approuvée :** Je valide

**Tableau de formalisation consécutive à la validation :**

| ID | Passif | Règle validée |
|--------|--------|--------|
| `MAGE-P1-001` | P1 - Critique de compétence | \+15 points de pourcentage |
| `MAGE-P1-002` | Groupe | `SKILL_CRITICAL_CHANCE` |
| `MAGE-P1-003` | Granularité | Un jet par impact de compétence éligible |
| `MAGE-P1-004` | Attaques normales, combos, contre-attaques | Exclues |
| `MAGE-P1-005` | Dégâts des acolytes | Exclus |
| `MAGE-P2-001` | P2 - ATQ | \+12 % |
| `MAGE-P2-002` | Groupe | `GLOBAL_ATTACK_PERCENT` |
| `MAGE-P2-003` | Application | Statistique ATQ effective du propriétaire |
| `MAGE-P2-004` | Autres bonus d'ATQ | Agrégation par le Modifier Engine |
| `MAGE-P2-005` | Dégâts indépendants de l'ATQ | Aucune amplification automatique |


#### T134 · SYS-002.D.12.5.11.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T134`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t134) — export ligne 45157; réponse ligne 45162.

**Prescription approuvée :** Validation SYS-002.D.12.5.11.1 : contrats des passifs Prophet = reference

**Tableau de formalisation consécutive à la validation :**

| ID | Passif | Contrat validé |
|--------|--------|--------|
| `MAGE-PRO-P3-001` | P3 - Régénération d'énergie | \+20 % dans `PATCH_REFERENCE` |
| `MAGE-PRO-P3-002` | Version historique | \+30 % dans `LEGACY` |
| `MAGE-PRO-P3-003` | Périmètre | Régénération des compétences actives équipées utilisant l'énergie |
| `MAGE-PRO-P3-004` | Suppression d'énergie | Prioritaire sur le bonus de régénération |
| `MAGE-PRO-P4-001` | P4 - Extension de durée | \+40 % dans `PATCH_REFERENCE`, +50 % dans `LEGACY` |
| `MAGE-PRO-P4-002` | Bonus de dégâts | \+10 % dans `PATCH_REFERENCE`, +30 % dans `LEGACY` |
| `MAGE-PRO-P4-003` | Blitz Assault | Durée non prolongée ; bonus offensif conservé |
| `MAGE-PRO-P4-004` | Effets périodiques | Échéances supplémentaires autorisées, sans double multiplication |
| `MAGE-PRO-P5-001` | P5 - Réduction de cooldown | -300 000 µs par nouvel étourdissement réussi |
| `MAGE-PRO-P5-002` | Déclencheur | `STUN_NEW_APPLICATION` causé directement par Prophet |
| `MAGE-PRO-P5-003` | Étourdissements AoE | Une réduction par cible nouvellement étourdie |
| `MAGE-PRO-P5-004` | Rafraîchissement d'un étourdissement existant | Aucun nouveau déclenchement |
| `MAGE-PRO-P5-005` | Cooldowns concernés | Compétences actives équipées uniquement |
| `MAGE-PRO-P5-006` | Cooldown minimum | Zéro, sans crédit négatif |
| `MAGE-PRO-P5-007` | Compétence nouvellement disponible | Activation différée jusqu'à la prochaine phase d'activation du scheduler |


#### T135 · SYS-002.D.12.5.19.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T135`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t135) — export ligne 45728; réponse ligne 45733.

**Prescription approuvée :** Validation SYS-002.D.12.5.19.1 : passifs Darklord = versioned

**Tableau de formalisation consécutive à la validation :**

| ID | Passif | Règle validée |
|--------|--------|--------|
| `MAGE-DARK-P3-001` | P3 - Critique de compétence | \+50 % de dégâts critiques de compétence |
| `MAGE-DARK-P3-002` | Groupe | `SKILL_CRITICAL_DAMAGE_BONUS` |
| `MAGE-DARK-P3-003` | Chance critique | Inchangée par P3 |
| `MAGE-DARK-P4-001` | P4 - Architecture | Profils mutuellement exclusifs |
| `MAGE-DARK-P4-002` | Profil initial | `PATCH_2024` |
| `MAGE-DARK-P4-003` | `PATCH_2024` | Composante supplémentaire de 20 % |
| `MAGE-DARK-P4-004` | `GUIDE_10` | Composante supplémentaire de 10 % |
| `MAGE-DARK-P4-005` | `LEGACY_LOW_HP` | Ancienne mécanique conditionnée aux PV de la cible |
| `MAGE-DARK-P4-006` | Immunité | Seule la composante supplémentaire contourne l'immunité ordinaire |
| `MAGE-DARK-P4-007` | Autres protections | Défense, résistances, boucliers et invulnérabilité absolue restent applicables |
| `MAGE-DARK-P4-008` | Critique | Réutilisation du résultat de la compétence, sans second tirage |
| `MAGE-DARK-P5-001` | P5 - Déclencheur | Activation effective d'une compétence active du propriétaire |
| `MAGE-DARK-P5-002` | Effet | Prochaine attaque normale : +100 % de dégâts |
| `MAGE-DARK-P5-003` | Charges | Une seule, non cumulable |
| `MAGE-DARK-P5-004` | Consommation | À l'engagement de la prochaine action normale |
| `MAGE-DARK-P5-005` | Attaque esquivée | Charge consommée |
| `MAGE-DARK-P5-006` | Durée | Jusqu'à consommation ou fin du combat |
| `MAGE-DARK-P5-007` | Combo | Non renforcé directement |


#### T136 · SYS-002.D.12.5.25.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T136`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t136) — export ligne 46344; réponse ligne 46349.

**Prescription approuvée :** Validation SYS-002.D.12.5.25.1 : compétences actives et Éveils Mage = versioned

**Tableau de formalisation consécutive à la validation :**

| ID | Mécanique | Décision validée |
|--------|--------|--------|
| `MAGE-ACT-010` | Compétence de classe | Météore AoE, indépendant des compétences gacha |
| `MAGE-ACT-011` | Profil initial | `PATCH_REFERENCE` |
| `MAGE-ACT-012` | Débuff initial | -20 points de résistance aux dégâts de compétence |
| `MAGE-ACT-013` | Durée standard | 5 secondes |
| `MAGE-ACT-014` | Durée après Éveil | 8 secondes |
| `MAGE-ACT-015` | Profil historique | `LEGACY_STUN`, allongement des étourdissements reçus de 30 % |
| `MAGE-ACT-016` | Réapplication du débuff | `UNIQUE_SOURCE_REFRESH` |
| `MAGE-PRO-AWK-012` | Éveil Prophet | Destruction des boucliers destructibles lors des impacts directs |
| `MAGE-PRO-AWK-013` | Durée initiale | 8 secondes |
| `MAGE-PRO-AWK-014` | Variante documentaire | 10 secondes |
| `MAGE-DARK-AWK-011` | Éveil Darklord | \+50 points au coefficient critique de compétence de base |
| `MAGE-DARK-AWK-012` | Durée | 10 secondes |
| `MAGE-DARK-AWK-013` | Cumul avec P3 | Autorisé, groupes de modificateurs distincts |
| `MAGE-TIME-001` | Cooldown initial de simulation | 12 secondes |
| `MAGE-TIME-002` | Délai d'impact initial | 1 seconde |
| `MAGE-TIME-003` | Rayon AoE initial | 3 unités logiques |
| `MAGE-TIME-004` | Nombre de cibles | Toutes les cibles éligibles dans la zone |


#### T137 · SYS-002.D.12.5.29.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T137`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t137) — export ligne 46793; réponse ligne 46798.

**Prescription approuvée :** Validation SYS-002.D.12.5.29.1 : clôture fonctionnelle Mage approuvée. Enregistre SYS-002.D.12.5 = functionally_specified avec calibration_pending, not_started et not_executed


#### T138 · SYS-002.D.12.6.7.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T138`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t138) — export ligne 47214; réponse ligne 47219.

**Prescription approuvée :** Validation SYS-002.D.12.6.7.1 : cartographie Spirit Channeler = provisional


#### T139 · SYS-002.D.12.6.13.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T139`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t139) — export ligne 47805; réponse ligne 47810.

**Prescription approuvée :** Validation SYS-002.D.12.6.13.1 : passifs communs Spirit Channeler = versioned

**Tableau de formalisation consécutive à la validation :**

| ID | Mécanique | Contrat validé |
|--------|--------|--------|
| `SPIRIT-P1-001` | Capacité Pal | \+1 emplacement |
| `SPIRIT-P1-002` | Capacité totale initiale | 6 Pals actifs |
| `SPIRIT-P1-003` | Héritage | Bonus unique conservé dans les deux branches |
| `SPIRIT-P1-004` | Changement de classe | Conservation du sixième Pal affecté |
| `SPIRIT-P1-005` | Emplacement inactif | Aucune contribution au combat |
| `SPIRIT-P1-006` | Retour à Spirit Channeler | Réactivation de l'affectation enregistrée |
| `SPIRIT-P2-001` | Vitesse d'attaque Pal initiale | \+0,1 % |
| `SPIRIT-P2-002` | Groupe | `PAL_BASE_ATTACK_SPEED_PERCENT` |
| `SPIRIT-P2-003` | Valeur interne | `10 BP` |
| `SPIRIT-P2-004` | Profil alternatif | `PREVIEW_FLAT_0_1` |
| `SPIRIT-P2-005` | Ignore-évasion Pal | \+10 points de pourcentage |
| `SPIRIT-P2-006` | Portée | Pals actifs appartenant au joueur |
| `SPIRIT-P2-007` | APS du personnage | Non affectée |
| `SPIRIT-P2-008` | Niveaux de déblocage P2-P4 | Configurables, non encore confirmés |


#### T140 · SYS-002.D.12.6.21.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T140`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t140) — export ligne 48512; réponse ligne 48517.

**Prescription approuvée :** Validation SYS-002.D.12.6.21.1 : passifs Beastmaster P3/P4/P5 = guide

**Tableau de formalisation consécutive à la validation :**

| ID | Passif | Règle validée |
|--------|--------|--------|
| `SPIRIT-BM-P3-001` | P3 - Critique Pal | \+25 points de probabilité |
| `SPIRIT-BM-P3-002` | Granularité | Un tirage critique par impact Pal éligible |
| `SPIRIT-BM-P3-003` | Bénéficiaires | Tous les Pals actifs du propriétaire |
| `SPIRIT-BM-P4-001` | P4 - Coefficient Pal | \+10 points au coefficient de dégâts |
| `SPIRIT-BM-P4-002` | Profil initial | `GUIDE_STATIC_10` |
| `SPIRIT-BM-P4-003` | Profil alternatif | `PREVIEW_2024_10_TO_20` |
| `SPIRIT-BM-P4-004` | P4 après Éveil, profil initial | \+10 points, inchangé |
| `SPIRIT-BM-P4-005` | P4 après Éveil, profil alternatif | \+20 points, remplaçant +10 |
| `SPIRIT-BM-P5-001` | P5 - Dégâts selon PV manquants | \+4 % par tranche complète de 10 % |
| `SPIRIT-BM-P5-002` | Référence | PV actuellement manquants du propriétaire |
| `SPIRIT-BM-P5-003` | Soins | Réduction dynamique du bonus |
| `SPIRIT-BM-P5-004` | Cumul | `DYNAMIC_MAGNITUDE_REPLACEMENT` |
| `SPIRIT-BM-P5-005` | Dégâts absorbés par bouclier | Aucun changement de P5 |


#### T141 · SYS-002.D.12.6.29.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T141`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t141) — export ligne 49147; réponse ligne 49152.

**Prescription approuvée :** Validation SYS-002.D.12.6.29.1 : passifs Supreme Spirit P3/P4/P5 = reference

**Tableau de formalisation consécutive à la validation :**

| ID | Passif | Contrat validé |
|--------|--------|--------|
| `SPIRIT-SS-P3-001` | P3 - Effets de déploiement | Magnitudes numériques éligibles augmentées de 20 % |
| `SPIRIT-SS-P3-002` | Sources éligibles | `NATIVE_PAL_DEPLOYMENT` uniquement |
| `SPIRIT-SS-P3-003` | Effets P4/P5 | Exclus de l'amplification P3 |
| `SPIRIT-SS-P3-004` | Application | Une seule transformation de magnitude, sans réamplification |
| `SPIRIT-SS-P4-001` | P4 avant Éveil | Examine `PAL_SLOT_01` |
| `SPIRIT-SS-P4-002` | P4 après Éveil | Examine `PAL_SLOT_01` et `PAL_SLOT_02` |
| `SPIRIT-SS-P4-003` | Position | Indices absolus, sans compactage |
| `SPIRIT-SS-P4-004` | Doublons | `UNIQUE_RACE_RULE`, sauf politique de cumul explicite |
| `SPIRIT-SS-P5-001` | P5 - Synergies | Calculées sur les Pals effectivement déployés |
| `SPIRIT-SS-P5-002` | Plusieurs synergies | `STACK_DISTINCT_RULES` |
| `SPIRIT-SS-P5-003` | Condition multiraciale | Instances distinctes nécessaires pour satisfaire plusieurs exigences |
| `SPIRIT-SS-P5-004` | Emplacements inactifs | Exclus des comptages |
| `SPIRIT-SS-P5-005` | Catalogue incomplet | `catalog_pending`, non exécutable pour les règles manquantes |


#### T142 · SYS-002.D.12.6.36.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T142`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t142) — export ligne 49744; réponse ligne 49749.

**Prescription approuvée :** Validation SYS-002.D.12.6.36.1 : compétences et Éveils Spirit Channeler = reference

**Tableau de formalisation consécutive à la validation :**

| Paramètre | Valeur | Provenance |
|--------|--------|--------|
| Cooldown de classe | 12 s | `designed` |
| Délai activation → impact | 250 ms | `designed` |
| Rayon AoE | 3 unités logiques | `designed` |
| Nombre de cibles AoE | Toutes les cibles éligibles | `designed` |


#### T143 · SYS-002.D.12.6.44.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T143`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t143) — export ligne 50427; réponse ligne 50432.

**Prescription approuvée :** Validation SYS-002.D.12.6.44.1 : clôture fonctionnelle de Spirit Channeler approuvée. Enregistre SYS-002.D.12.6 = functionally_specified, avec unlock_calibration_pending, catalog_pending, calibration_pending, not_started et not_executed. Réalise ensuite une revue consolidée des quatre classes et identifie le prochain chantier prioritaire du GDD

**Tableau de formalisation consécutive à la validation :**

| Module | Famille | Branches finales | Statut |
|--------|--------|--------|--------|
| `SYS-002.D.12.3` | Guerrier | Martial Sage / Warbringer | `functionally_specified` |
| `SYS-002.D.12.4` | Archer | Sacred Hunter / Plume Monarch | `functionally_specified` |
| `SYS-002.D.12.5` | Mage | Prophet / Darklord | `functionally_specified` |
| `SYS-002.D.12.6` | Spirit Channeler | Beastmaster / Supreme Spirit | `functionally_specified` |


### 13 - Moteur de combat partagé et contrats transversaux

#### T144 · SYS-002.D.13

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T144`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t144) — export ligne 50790; réponse ligne 50795.

**Prescription approuvée :** Je valide l'ouverture de SYS-002.D.13 — Shared Combat Engine Specification. Commence par SYS-002.D.13.1 : audit et formalisation du modèle d'acteurs, d'actions et d'événements, avec causalité, contrats, invariants et tests. Ne commence pas l'implémentation


#### T145 · SYS-002.D.13.1.9.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T145`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t145) — export ligne 51814; réponse ligne 51819.

**Prescription approuvée :** Je valide SYS-002.D.13.1.9.1 : les douze contrats CORE-001 à CORE-012 du modèle partagé d'acteurs, d'actions, d'opérations programmées et d'événements. Enregistre D.13.1 = functionally_specified, avec not_started et not_executed. Passe ensuite à SYS-002.D.13.2 — Action Lifecycle, en approfondissant les transitions, annulations partielles, engagements de ressources et impacts différés, sans implémentation


#### T146 · SYS-002.D.13.2.10.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T146`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t146) — export ligne 52736; réponse ligne 52741.

**Prescription approuvée :** Je valide SYS-002.D.13.2.10.1 : les seize contrats LIFE-001 à LIFE-016 du cycle de vie des actions. Enregistre SYS-002.D.13.2 = functionally_specified avec not_started et not_executed. Passe ensuite à SYS-002.D.13.3 — Combat Scheduler : audite l'ordre total des phases, les collisions au même timestamp, le traitement des réactions, les politiques RNG et le déterminisme, sans implémentation


#### T147 · SYS-002.D.13.3.9.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T147`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t147) — export ligne 53559; réponse ligne 53564.

**Prescription approuvée :** Je valide SYS-002.D.13.3.9.1 : les dix-huit contrats SCHED-001 à SCHED-018 du Combat Scheduler. Enregistre SYS-002.D.13.3 = functionally_specified avec not_started et not_executed. Passe ensuite à SYS-002.D.13.4 — Damage Resolution : audite le pipeline des dégâts, les catégories de dégâts, les critiques, la Défense, les résistances, les boucliers, les immunités, les dégâts proportionnels aux PV et les règles d'arrondi, sans implémentation


#### T148 · SYS-002.D.13.4.14.1

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T148`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t148) — export ligne 54827; réponse ligne 54832.

**Prescription approuvée :** Je valide SYS-002.D.13.4.14.1 : les vingt-quatre contrats DMG-001 à DMG-024 du Damage Resolution Engine. Enregistre SYS-002.D.13.4 = functionally_specified avec defense_calibration_pending, damage_mode_calibration_pending, calibration_pending, not_started et not_executed. Passe ensuite à SYS-002.D.13.5 — Modifier & Snapshot Engine : audite l'agrégation des modificateurs, les groupes, les priorités, les snapshots offensifs, les effets temporaires, les rafraîchissements et la persistance après mort, sans implémentation


#### T149 · SYS-002.D.13.5

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T149`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t149) — export ligne 55942; réponse ligne 55947.

**Prescription approuvée :** Oui je valide

**Tableau de formalisation consécutive à la validation :**

| Module | Statut |
|--------|--------|
| `D.13.1` - Actors, Actions &amp; Events | `functionally_specified` |
| `D.13.2` - Action Lifecycle | `functionally_specified` |
| `D.13.3` - Combat Scheduler | `functionally_specified` |
| `D.13.4` - Damage Resolution | `functionally_specified` |
| `D.13.5` - Modifier &amp; Snapshot Engine | `functionally_specified` |
| `D.13.6` - Pal Combat Integration | `under_audit` |
| Implémentation | `not_started` |
| Tests | `not_executed` |


#### T150 · SYS-002.D.13.6

**Autorité :** `APPROBATION_EXPLICITE` · **Traçabilité :** [`T150`](GDD_SYS-002_RECONSTITUE_2026-11-21.md#t150) — export ligne 57037; réponse ligne 57042.

**Prescription approuvée :** Je valide

**Tableau de formalisation consécutive à la validation :**

| Module | Statut |
|--------|--------|
| `D.13.1` - Actors, Actions &amp; Events | `functionally_specified` |
| `D.13.2` - Action Lifecycle | `functionally_specified` |
| `D.13.3` - Combat Scheduler | `functionally_specified` |
| `D.13.4` - Damage Resolution | `functionally_specified` |
| `D.13.5` - Modifier &amp; Snapshot Engine | `functionally_specified` |
| `D.13.6` - Pal Combat Integration | `functionally_specified` |
| `D.13.7` - Combat Lifecycle | `under_audit` |
| `D.13.8` - Cross-Class Acceptance Tests | `not_started` |


---

## 3. Shared Combat Engine — 102 contrats expressément approuvés

L'acceptation des blocs de contrats est documentée dans les tours `T145` à `T150`. Le texte de chaque contrat ci-dessous est issu de la dernière table de contrats présentée juste avant la validation, sans réécriture des libellés. Les dossiers techniques détaillés ratifiés sont reproduits dans le fichier d'annexe associé. Aucun contrat `CLF` n'entre dans le décompte.

### SYS-002.D.13.1 — Combat Actor, Action & Event Model

**Décision :** `SYS-002.D.13.1.9.1` approuvée `T145` sur spécification `T144`. **Statut :** `functionally_specified` / `not_started` / `not_executed`.

| Contrat | Règle normative validée |
|:--|:--|
| `CORE-001` | Acteurs identifiés indépendamment de leurs définitions persistantes |
| `CORE-002` | Source et propriétaire explicitement distincts |
| `CORE-003` | Capacités des acteurs configurables, notamment pour les Pals |
| `CORE-004` | Actions, opérations programmées et événements séparés |
| `CORE-005` | Engagement d'une action distinct de ses impacts |
| `CORE-006` | Annulation non rétroactive, avec résolution partielle possible |
| `CORE-007` | Graphe causal acyclique avec actions parentes et événements déclencheurs |
| `CORE-008` | Événements de domaine immuables et traces diagnostiques séparées |
| `CORE-009` | Déduplication déclarée par mécanique |
| `CORE-010` | Identifiants et ordre d'exécution déterministes |
| `CORE-011` | Échéances invalidables par génération |
| `CORE-012` | Version de configuration figée par combat |

### SYS-002.D.13.2 — Action Lifecycle

**Décision :** `SYS-002.D.13.2.10.1` approuvée `T146` sur spécification `T145`. **Statut :** `functionally_specified` / `not_started` / `not_executed`.

| Contrat | Règle normative validée |
|:--|:--|
| `LIFE-001` | Sept états d'action, transitions strictement contrôlées |
| `LIFE-002` | Terminalité distincte du résultat effectif |
| `LIFE-003` | Compteurs d'opérations cohérents et vérifiables |
| `LIFE-004` | Engagement atomique des ressources, cooldowns et effets d'activation |
| `LIFE-005` | Rejet sans coût ni cooldown |
| `LIFE-006` | Absence de remboursement implicite après engagement |
| `LIFE-007` | Capture offensive après installation des buffs d'activation |
| `LIFE-008` | Résolution partielle possible, sans annulation rétroactive |
| `LIFE-009` | Opérations `EXECUTED`, `SKIPPED`, `CANCELLED` et `STALE` distinctes |
| `LIFE-010` | Annulation des opérations différées selon leur politique de survie |
| `LIFE-011` | Maintien des réactions immédiates déjà déclenchées |
| `LIFE-012` | Impossibilité d'engager une action ordinaire après `DEATH_PENDING` |
| `LIFE-013` | Durée de vie des effets indépendante de celle des actions |
| `LIFE-014` | Actions enfants indépendantes de la terminalité du parent |
| `LIFE-015` | Annulation avant la décision de combo empêchant la création du combo |
| `LIFE-016` | Versionnement et traçabilité de tous les engagements et annulations |

### SYS-002.D.13.3 — Combat Scheduler

**Décision :** `SYS-002.D.13.3.9.1` approuvée `T147` sur spécification `T146`. **Statut :** `functionally_specified` / `not_started` / `not_executed`.

| Contrat | Règle normative validée |
|:--|:--|
| `SCHED-001` | Horloge logique en microsecondes entières |
| `SCHED-002` | Exécution événementielle, sans dépendance au framerate |
| `SCHED-003` | Six phases ordonnées : expirations, engagements, impacts de classe, autres impacts, réactions résiduelles, finalisation |
| `SCHED-004` | Disponibilités temporelles traitées avant les engagements |
| `SCHED-005` | Priorité des compétences de classe sur les nouvelles actions normales et Pal |
| `SCHED-006` | Une seule activation ordinaire par acteur et timestamp |
| `SCHED-007` | Clôture des réactions immédiates après chaque opération d'impact |
| `SCHED-008` | Atomicité d'une opération AoE sur son ensemble de cibles |
| `SCHED-009` | Impacts indépendants résolus séquentiellement selon un ordre total |
| `SCHED-010` | Ordre stable des opérations et des cibles |
| `SCHED-011` | Aucun retour rétroactif vers une phase clôturée |
| `SCHED-012` | Nouvelle décision au prochain instant logique admissible |
| `SCHED-013` | Politique RNG déterministe par identité de décision |
| `SCHED-014` | Aucun tirage RNG pour une décision inéligible |
| `SCHED-015` | Résultat RNG unique et reproductible par décision |
| `SCHED-016` | Règles de calcul, ordre des événements et algorithme RNG versionnés |
| `SCHED-017` | Journal des événements de domaine distinct des traces diagnostiques |
| `SCHED-018` | Reproductibilité définie par l'ensemble des entrées initiales et des commandes |

### SYS-002.D.13.4 — Damage Resolution Engine

**Décision :** `SYS-002.D.13.4.14.1` approuvée `T148` sur spécification `T147`. **Statut :** `functionally_specified` / `not_started` / `not_executed`.

| Contrat | Règle normative validée |
|:--|:--|
| `DMG-001` | Les dégâts sont décomposés en composantes identifiées et typées |
| `DMG-002` | Origine, catégorie offensive, groupe de scaling et profil défensif sont séparés |
| `DMG-003` | Un impact confirme la touche avant la résolution des dégâts |
| `DMG-004` | Les critiques sont résolus avant les mitigations |
| `DMG-005` | Les composantes peuvent hériter d'un résultat critique sans nouveau tirage |
| `DMG-006` | La DEF utilise une formule versionnée, jamais implicite |
| `DMG-007` | Les résistances sont appliquées par groupe éligible |
| `DMG-008` | Les résistances du profil initial sont bornées entre 0 et 100 % |
| `DMG-009` | Les bonus de dégâts reçus sont distincts des réductions de résistance |
| `DMG-010` | Les immunités sont évaluées par composante |
| `DMG-011` | Le contournement d'immunité est explicite et limité aux catégories autorisées |
| `DMG-012` | L'invulnérabilité absolue protège contre les effets hostiles, sauf exception explicite |
| `DMG-013` | Les boucliers sont des instances indépendantes avec un ordre d'absorption stable |
| `DMG-014` | La destruction des boucliers précède leur absorption sur un impact admissible |
| `DMG-015` | Les pertes de capacité de bouclier sont distinctes des pertes de PV |
| `DMG-016` | Les dégâts proportionnels aux PV utilisent une référence pré-impact explicite |
| `DMG-017` | Les composantes d'un même impact suivent un ordre stable |
| `DMG-018` | Les dégâts supplémentaires ne produisent pas de critique ou de récursion implicite |
| `DMG-019` | Les calculs intermédiaires utilisent une arithmétique déterministe |
| `DMG-020` | La quantification initiale utilise `FIXED_POINT_FLOOR_FINAL` par composante |
| `DMG-021` | Les dégâts effectifs ne peuvent pas dépasser les PV disponibles |
| `DMG-022` | Les événements de touche, critique, bouclier et dégâts PV sont distincts |
| `DMG-023` | Le profil de dégâts, les formules et leurs politiques d'arrondi sont versionnés |
| `DMG-024` | Toute formule ou donnée indispensable manquante empêche l'exécution du profil |

### SYS-002.D.13.5 — Modifier & Snapshot Engine

**Décision :** `SYS-002.D.13.5.12.1` approuvée `T149` sur spécification `T148`. **Statut :** `functionally_specified` / `not_started` / `not_executed`.

| Contrat | Règle normative validée |
|:--|:--|
| `MOD-001` | Modificateurs identifiés, typés et associés à une source |
| `MOD-002` | Agrégation calculée depuis les contributions, sans mutation cumulative des statistiques de base |
| `MOD-003` | Opérations mathématiques et unités explicites |
| `MOD-004` | Ordre stable : transformation des contributions, agrégation des groupes, composition, bornage |
| `MOD-005` | Groupes distincts pour les statistiques offensives, défensives, critiques, Pal et ressources |
| `MOD-006` | Rejet des remplacements de même priorité incompatibles |
| `MOD-007` | Politiques `STATIC_WHILE_ELIGIBLE`, `DYNAMIC_STATE_DERIVED` et `APPLICATION_SNAPSHOT` |
| `MOD-008` | Recalcul dynamique par graphe de dépendances acyclique |
| `MOD-009` | Amplification des effets natifs Supreme Spirit P3 avant agrégation, une seule fois |
| `MOD-010` | Snapshot offensif après les effets d'activation, immuable ensuite |
| `MOD-011` | Nouveau snapshot pour chaque action enfant autonome |
| `MOD-012` | Défenses, immunités et boucliers évalués à l'impact |
| `MOD-013` | Instances d'effets distinctes des actions qui les créent |
| `MOD-014` | Durées semi-ouvertes, expirations prioritaires |
| `MOD-015` | `UNIQUE_SOURCE_REFRESH` avec clé de source stable |
| `MOD-016` | Rafraîchissement remplaçant durée et magnitude, sans cumul implicite |
| `MOD-017` | Générations invalidant les anciennes échéances |
| `MOD-018` | Rafraîchissement périodique conservant sa phase de ticks par défaut |
| `MOD-019` | Persistance après mort explicitement définie par catégorie d'effet |
| `MOD-020` | Nettoyage après résolution des réactions mortelles admissibles |
| `MOD-021` | Capacités non numériques et charges consommables séparées des bonus statistiques |
| `MOD-022` | Charge Darklord P5 capturée et consommée atomiquement à l'engagement |
| `MOD-023` | Aucun recalcul rétroactif des actions déjà engagées |
| `MOD-024` | Profils de groupes, unités, durées et politiques d'effets versionnés |

### SYS-002.D.13.6 — Pal Combat Integration

**Décision :** `SYS-002.D.13.6.11.1` approuvée `T150` sur spécification `T149`. **Statut :** `functionally_specified` / `not_started` / `not_executed`.

| Contrat | Règle normative validée |
|:--|:--|
| `PAL-001` | Les Pals sont des acteurs offensifs autonomes, dépendants d'un propriétaire |
| `PAL-002` | Les statistiques Pal et effets de déploiement utilisent les modificateurs partagés |
| `PAL-003` | Chaque Pal possède une progression d'attaque individuelle, conservée aux changements d'APS |
| `PAL-004` | Les attaques et combos Pal réutilisent les actions parentes, impacts enfants et RNG déterministes |
| `PAL-005` | Le ciblage Pal est explicite et aucun retargeting n'est implicite |
| `PAL-006` | Les passifs Beastmaster/Supreme Spirit utilisent les contrats partagés sans règles parallèles |
| `PAL-007` | Mort du propriétaire : annulation des actions Pal restantes, sans effacer les faits déjà produits |
| `PAL-008` | Les profils Pal et synergies incomplets ne peuvent pas produire de règles exécutables |

## 4. Statuts fonctionnels approuvés (pas des résultats de tests)

| Composant | Décision ratifiée | Contrats approuvés | Fonctionnel | Implémentation | Tests |
|:--|:--|:--|:--|:--|:--|
| `SYS-002.D.13.1` | `SYS-002.D.13.1.9.1` (`T145`) | `CORE-001..CORE-012` (12) | `functionally_specified` | `not_started` | `not_executed` |
| `SYS-002.D.13.2` | `SYS-002.D.13.2.10.1` (`T146`) | `LIFE-001..LIFE-016` (16) | `functionally_specified` | `not_started` | `not_executed` |
| `SYS-002.D.13.3` | `SYS-002.D.13.3.9.1` (`T147`) | `SCHED-001..SCHED-018` (18) | `functionally_specified` | `not_started` | `not_executed` |
| `SYS-002.D.13.4` | `SYS-002.D.13.4.14.1` (`T148`) | `DMG-001..DMG-024` (24) | `functionally_specified` | `not_started` | `not_executed` |
| `SYS-002.D.13.5` | `SYS-002.D.13.5.12.1` (`T149`) | `MOD-001..MOD-024` (24) | `functionally_specified` | `not_started` | `not_executed` |
| `SYS-002.D.13.6` | `SYS-002.D.13.6.11.1` (`T150`) | `PAL-001..PAL-008` (8) | `functionally_specified` | `not_started` | `not_executed` |

**Réserves de calibration présentes dans les validations :** `defense_calibration_pending`, `damage_mode_calibration_pending`, `calibration_pending`, `unlock_calibration_pending`, `catalog_pending`, `pending_data_completion` selon le sous-système concerné. Ce sont des **statuts de non-complétude** et non des valeurs de remplacement. Aucun résultat de simulation ni de test n'est revendiqué.

## 5. Exclusions contrôlées

Le présent GDD **ne contient pas** : les 20 contrats `CLF-001..CLF-020` de `SYS-002.D.13.7.12.1` (seulement proposés à `T150`), les spécifications de `D.13.8` (non commencées), le choix initial Godot remplacé par Unity, les courbes exponentielles/convexes des acolytes abandonnées, la fusion à partir de cartes non débloquées, ou des résultats de tests fictifs.

Toute décision ultérieure devra être ajoutée avec un identifiant stable, une preuve d'approbation, une politique de remplacement explicite, un état de calibration et un statut d'exécution distinct.

## 6. Documents de preuve liés

- `GDD_SYS-002_ANNEXE_CONTRATS_RATIFIES_2026-11-21.md` : dossiers techniques détaillés ratifiés D.13.1–D.13.6.
- `GDD_SYS-002_ANNEXE_PRESCRIPTIONS_PROPRIETAIRE_2026-11-21.md` : intégralité des prescriptions longues et de leurs précisions, avec le tour source.
- `GDD_SYS-002_REGISTRE_NORMATIF_2026-11-21.csv` : chaque intervention sélectionnée, sa nature et sa traçabilité.
- `GDD_SYS-002_CONTRATS_APPROUVES_2026-11-21.csv` : chaque contrat approuvé en entrée séparée.
- `GDD_SYS-002_RECONSTITUE_2026-11-21.md` : reconstruction historique intégrale, à consulter uniquement pour vérification.
- `ChatGPT-Activation du mode absolu-20261121-2332.md` : export original, immuable.
