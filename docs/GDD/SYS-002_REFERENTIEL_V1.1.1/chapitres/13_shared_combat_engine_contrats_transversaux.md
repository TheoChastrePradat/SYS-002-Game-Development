# Chapitre 13 — Shared Combat Engine — contrats transversaux

**Autorité :** décisions expressément approuvées dans la conversation source. Les modèles obsolètes sont remplacés par les rectifications ultérieures ; les paramètres provisoires restent provisoires.

**Statut du chapitre :** `functionally_specified` pour ses spécifications validées ; aucune exécution de test ou implémentation ne découle de ce statut.

**Traçabilité :** 7 décision(s) du propriétaire. Toutes les références `Txxx` renvoient à `references/HISTORIQUE_SOURCE_ORIGINAL.md`.

## Contrats ratifiés

Les modules `D.13.1` à `D.13.6` ont été approuvés en six étapes successives. Total ratifié : **102 contrats**, séparés par domaine. Les textes détaillés, équations et diagrammes approuvés du bloc partagé figurent dans `annexes/SPECIFICATIONS_DETAILLEES_D13.1_A_D13.6.md`.

| Domaine | Contrats | Décision utilisateur | Statut |
|---|---:|---|---|
| D.13.1 — Actor/Action/Event | CORE-001…CORE-012 (12) | T145 | `functionally_specified` |
| D.13.2 — Action Lifecycle | LIFE-001…LIFE-016 (16) | T146 | `functionally_specified` |
| D.13.3 — Scheduler | SCHED-001…SCHED-018 (18) | T147 | `functionally_specified` |
| D.13.4 — Damage Resolution | DMG-001…DMG-024 (24) | T148 | `functionally_specified` |
| D.13.5 — Modifier & Snapshot | MOD-001…MOD-024 (24) | T149 | `functionally_specified` |
| D.13.6 — Pal Integration | PAL-001…PAL-008 (8) | T150 | `functionally_specified` |

**D.13.7** — 20 contrats CLF en attente de validation, donc **non inclus**. **D.13.8** — non commencé.


### SYS-002.D.13.1 — Combat Actor, Action & Event Model

**Validation :** `SYS-002.D.13.1.9.1` (`T145`).

| Contrat | Clause normative ratifiée |
|---|---|
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

**Validation :** `SYS-002.D.13.2.10.1` (`T146`).

| Contrat | Clause normative ratifiée |
|---|---|
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

**Validation :** `SYS-002.D.13.3.9.1` (`T147`).

| Contrat | Clause normative ratifiée |
|---|---|
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

**Validation :** `SYS-002.D.13.4.14.1` (`T148`).

| Contrat | Clause normative ratifiée |
|---|---|
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

**Validation :** `SYS-002.D.13.5.12.1` (`T149`).

| Contrat | Clause normative ratifiée |
|---|---|
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

**Validation :** `SYS-002.D.13.6.11.1` (`T150`).

| Contrat | Clause normative ratifiée |
|---|---|
| `PAL-001` | Les Pals sont des acteurs offensifs autonomes, dépendants d'un propriétaire |
| `PAL-002` | Les statistiques Pal et effets de déploiement utilisent les modificateurs partagés |
| `PAL-003` | Chaque Pal possède une progression d'attaque individuelle, conservée aux changements d'APS |
| `PAL-004` | Les attaques et combos Pal réutilisent les actions parentes, impacts enfants et RNG déterministes |
| `PAL-005` | Le ciblage Pal est explicite et aucun retargeting n'est implicite |
| `PAL-006` | Les passifs Beastmaster/Supreme Spirit utilisent les contrats partagés sans règles parallèles |
| `PAL-007` | Mort du propriétaire : annulation des actions Pal restantes, sans effacer les faits déjà produits |
| `PAL-008` | Les profils Pal et synergies incomplets ne peuvent pas produire de règles exécutables |


## Registre détaillé des décisions approuvées


### SYS-002.D.13 · T144 · 21/11/2026 19:32:14

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 50790 · **Ligne de formalisation :** 50795.

**Décision / prescription originale (texte intégral du propriétaire) :**

Je valide l'ouverture de SYS-002.D.13 — Shared Combat Engine Specification. Commence par SYS-002.D.13.1 : audit et formalisation du modèle d'acteurs, d'actions et d'événements, avec causalité, contrats, invariants et tests. Ne commence pas l'implémentation.


**Source technique :** réponse consécutive et proposition précédant cette validation, consultables dans l’historique original. Aucun extrait automatique n’a été retenu faute de délimitation non ambiguë.


### SYS-002.D.13.1.9.1 · T145 · 21/11/2026 19:40:09

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 51814 · **Ligne de formalisation :** 51819.

**Décision / prescription originale (texte intégral du propriétaire) :**

Je valide SYS-002.D.13.1.9.1 : les douze contrats CORE-001 à CORE-012 du modèle partagé d'acteurs, d'actions, d'opérations programmées et d'événements. Enregistre D.13.1 = functionally_specified, avec not_started et not_executed. Passe ensuite à SYS-002.D.13.2 — Action Lifecycle, en approfondissant les transitions, annulations partielles, engagements de ressources et impacts différés, sans implémentation.


**Source technique :** réponse consécutive et proposition précédant cette validation, consultables dans l’historique original. Aucun extrait automatique n’a été retenu faute de délimitation non ambiguë.


### SYS-002.D.13.2.10.1 · T146 · 21/11/2026 19:43:42

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 52736 · **Ligne de formalisation :** 52741.

**Décision / prescription originale (texte intégral du propriétaire) :**

Je valide SYS-002.D.13.2.10.1 : les seize contrats LIFE-001 à LIFE-016 du cycle de vie des actions. Enregistre SYS-002.D.13.2 = functionally_specified avec not_started et not_executed. Passe ensuite à SYS-002.D.13.3 — Combat Scheduler : audite l'ordre total des phases, les collisions au même timestamp, le traitement des réactions, les politiques RNG et le déterminisme, sans implémentation.


**Source technique :** réponse consécutive et proposition précédant cette validation, consultables dans l’historique original. Aucun extrait automatique n’a été retenu faute de délimitation non ambiguë.


### SYS-002.D.13.3.9.1 · T147 · 21/11/2026 19:48:59

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 53559 · **Ligne de formalisation :** 53564.

**Décision / prescription originale (texte intégral du propriétaire) :**

Je valide SYS-002.D.13.3.9.1 : les dix-huit contrats SCHED-001 à SCHED-018 du Combat Scheduler. Enregistre SYS-002.D.13.3 = functionally_specified avec not_started et not_executed. Passe ensuite à SYS-002.D.13.4 — Damage Resolution : audite le pipeline des dégâts, les catégories de dégâts, les critiques, la Défense, les résistances, les boucliers, les immunités, les dégâts proportionnels aux PV et les règles d'arrondi, sans implémentation.


**Source technique :** réponse consécutive et proposition précédant cette validation, consultables dans l’historique original. Aucun extrait automatique n’a été retenu faute de délimitation non ambiguë.


### SYS-002.D.13.4.14.1 · T148 · 21/11/2026 19:54:12

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 54827 · **Ligne de formalisation :** 54832.

**Décision / prescription originale (texte intégral du propriétaire) :**

Je valide SYS-002.D.13.4.14.1 : les vingt-quatre contrats DMG-001 à DMG-024 du Damage Resolution Engine. Enregistre SYS-002.D.13.4 = functionally_specified avec defense_calibration_pending, damage_mode_calibration_pending, calibration_pending, not_started et not_executed. Passe ensuite à SYS-002.D.13.5 — Modifier & Snapshot Engine : audite l'agrégation des modificateurs, les groupes, les priorités, les snapshots offensifs, les effets temporaires, les rafraîchissements et la persistance après mort, sans implémentation.


**Source technique :** réponse consécutive et proposition précédant cette validation, consultables dans l’historique original. Aucun extrait automatique n’a été retenu faute de délimitation non ambiguë.


### SYS-002.D.13.5 · T149 · 21/11/2026 22:22:26

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 55942 · **Ligne de formalisation :** 55947.

**Décision / prescription originale (texte intégral du propriétaire) :**

Oui je valide


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# SYS-002.D.13.5 - Clôture du Modifier &amp; Snapshot Engine

**Décision validée : `SYS-002.D.13.5.12.1`.**

Les 24 contrats `MOD-001` à `MOD-024` sont intégrés au référentiel du GDD. Le moteur de modificateurs et de snapshots est désormais **fonctionnellement spécifié**.

```yaml
decision_id: SYS-002.D.13.5.12.1
module_id: SYS-002.D.13.5
module_name: Modifier & Snapshot Engine

status:
  functional: functionally_specified
  implementation: not_started
  tests: not_executed

approved_contracts:
  first: MOD-001
  last: MOD-024
  count: 24

validated_policies:
  aggregation: GROUP_BASED_DETERMINISTIC
  offensive_snapshots: IMMUTABLE_AFTER_COMMIT
  dynamic_modifiers: DEPENDENCY_DRIVEN_REPLACEMENT
  effect_refresh: VERSIONED_GENERATION
  periodic_refresh: PRESERVE_TICK_PHASE_BY_DEFAULT
  post_death_effects: EXPLICIT_PERSISTENCE_POLICY
  consumable_charges: ATOMIC_CAPTURE_AND_CONSUME
```

L'engagement d'une action capture ses statistiques offensives après installation des effets d'activation. Les changements ultérieurs n'affectent que les actions futures. Les défenses, immunités et boucliers continuent d'être résolus à l'impact.

Les effets temporaires disposent d'un cycle de vie indépendant de l'action créatrice ; leur expiration, leur rafraîchissement et leur suppression suivent des règles explicites.

## État du moteur partagé

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

---

</details>


### SYS-002.D.13.6 · T150 · 21/11/2026 22:34:39

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 57037 · **Ligne de formalisation :** 57042.

**Décision / prescription originale (texte intégral du propriétaire) :**

Je valide


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# SYS-002.D.13.6 - Clôture de Pal Combat Integration

**Décision validée : `SYS-002.D.13.6.11.1`.**

Les huit contrats `PAL-001` à `PAL-008` sont intégrés au référentiel du GDD. Les règles de déploiement, de cadence, d'attaque, de combo et de dépendance au propriétaire sont approuvées.

```yaml
decision_id: SYS-002.D.13.6.11.1
module_id: SYS-002.D.13.6
module_name: Pal Combat Integration

status:
  functional: functionally_specified
  catalog: catalog_pending
  calibration: calibration_pending
  implementation: not_started
  tests: not_executed

approved_contracts:
  first: PAL-001
  last: PAL-008
  count: 8
```

Cet enregistrement concerne le GDD suivi dans notre conversation ; aucun fichier ni dépôt externe n'a été modifié.

## État consolidé du Shared Combat Engine

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

Le moteur Pal et les quatre familles de classes disposent désormais de contrats compatibles. Le prochain problème consiste à déterminer **à quel moment un acteur meurt définitivement, quand le combat s'arrête et quelles conséquences restent autorisées pendant sa clôture**.

---

</details>

