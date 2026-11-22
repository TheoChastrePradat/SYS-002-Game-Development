# Chapitre 06 — Modificateurs, groupes et priorités

**Autorité :** décisions expressément approuvées dans la conversation source. Les modèles obsolètes sont remplacés par les rectifications ultérieures ; les paramètres provisoires restent provisoires.

**Statut du chapitre :** `functionally_specified` pour ses spécifications validées ; aucune exécution de test ou implémentation ne découle de ce statut.

**Traçabilité :** 4 décision(s) du propriétaire. Toutes les références `Txxx` renvoient à `references/HISTORIQUE_SOURCE_ORIGINAL.md`.


## Registre détaillé des décisions approuvées


### SYS-002.D.6.1 · T017 · 17/11/2026 20:52:02

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 4876 · **Ligne de formalisation :** 4881.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.6.1 : groupes = explicit ; bonus plats = before ; cumul pourcentages = group ; groupe manquant = reject ; observations = Aucune. Formalise les décisions et poursuis avec SYS-002.D.6.2.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.6.1

(Validé) (Version 1.0)

| Élément | Décision |
|--------|--------|
| Groupes de cumul | Explicitement configurés |
| Bonus plats | Avant les bonus en pourcentage |
| Bonus d'un même groupe | Additifs |
| Groupes indépendants | Multiplicatifs |
| Groupe manquant | Rejet du modificateur |

## 1.1 Contrat du Modifier Resolver

Chaque modificateur devra obligatoirement posséder :

- Un identifiant unique.
- Un attribut cible.
- Une opération.
- Une valeur.
- Un groupe de cumul.
- Une portée d'application.
- Des conditions éventuelles.
- Une durée éventuelle.

Les opérations autorisées sont :

| Opération | Description |
|--------|--------|
| `ADD_FLAT` | Ajout d'une valeur fixe |
| `ADD_PERCENT` | Ajout d'un pourcentage |
| `MULTIPLY` | Multiplication indépendante |
| `OVERRIDE` | Remplacement selon une priorité explicite |

Tout modificateur incomplet sera rejeté lors de la validation des données.

---

</details>


### SYS-002.D.6.2 · T018 · 17/11/2026 21:12:09

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 5222 · **Ligne de formalisation :** 5227.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.6.2 : cumul attaque/cible = multiply ; cumul résistances même famille = family ; position critique = after_global ; augmentation/réduction finale = independent ; observations = Aucune. Formalise les décisions et poursuis selon le protocole.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.6.2

(Validé) (Version 1.0)

## 1.1 Décisions enregistrées

| Élément | Décision |
|--------|--------|
| Bonus attaque / cible | Multiplicatifs indépendants |
| Sources d'une même résistance | Additives |
| Familles de résistances différentes | Multiplicatives |
| Position du critique | Après résistances globales |
| Augmentation finale | Multiplicateur indépendant |
| Réduction finale | Multiplicateur indépendant |

## 1.2 Formule consolidée

Nous retenons :

$$
D_{\text{pré-crit}}=
D_0\times M_{\text{DEF}}
\times M_{\text{pen}}
\times M_{\text{attaque}}
\times M_{\text{cible}}
\times M_{\text{résistances}}
$$

Puis :

$$
D_{\text{pré-final}}=
D_{\text{pré-crit}}\times M_{\text{crit}}
$$

Et enfin :

$$
\boxed{
D_{\text{final}}=
D_{\text{pré-final}}
\times(1+A_{\text{final}})
\times(1-R_{\text{final}})
}
$$

Les bonus spécifiques à l'attaque et à la cible sont indépendants. Une compétence contre un boss bénéficie donc des deux catégories.

Les sources d'une même famille de résistance sont additionnées avant application. Les familles indépendantes sont ensuite multipliées.

## 1.3 Correction d'un exemple numérique

Une erreur arithmétique figurait dans l'exemple précédent.

Pour 10 000 dégâts de base, avec :

- Bonus compétence : +30 %.
- Bonus boss : +20 %.
- Résistance compétence : 15 %.
- Résistance boss : 10 %.
- Réduction globale : 5 %.

Le résultat correct est :

$$
10000\times1,30\times1,20
\times0,85\times0,90\times0,95
$$

(11 337,30 dégâts)

Le calculateur devra produire une décomposition de chaque multiplicateur afin de rendre les résultats vérifiables.

---

</details>


### SYS-002.D.6.3 · T019 · 18/11/2026 14:07:29

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 5632 · **Ligne de formalisation :** 5637.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.6.3 : OVERRIDE = base ; conflit même priorité = reject ; politique de cumul = explicit ; valeurs négatives = allow_clamp ; expiration = before ; UNIQUE_SOURCE = refresh ; observations = Afin d'être en accord, si plusieurs bonus se succèdent par rapport au même attribut, il doivent s'additionner, pas seulement choisir le dernier ou le plus élevé. Par exemple si une compétence applique +5% de vitesse d'attaque pendant 3 secondes et qu'une autre compétence simultanément active +3% de vitesse d'attaque pendant 6 secondes, le bonus sera de 8% pendant 3 secondes puis redescendra à 3% pour les 3 secondes restantes. Est ce clair ?. Formalise les décisions et poursuis selon le protocole.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD — SYS-002.D.6.3

(Validé) (Version 1.1)

## 1.1 Décisions enregistrées

| Élément | Décision |
|--------|--------|
| `OVERRIDE` | Remplace la valeur de base |
| Conflit de priorité identique | Rejet |
| Politique de cumul | Obligatoire et explicite |
| Valeurs négatives | Autorisées, avec contraintes par attribut |
| Expiration | Avant les événements au même timestamp |
| `UNIQUE_SOURCE` | Actualisation de la durée |

## 1.2 Nouvelle règle : cumul des effets provenant de sources différentes

Les bonus provenant de sources différentes doivent pouvoir coexister et s'additionner lorsqu'ils appartiennent au même groupe de cumul.

Ton exemple devient une règle de référence du GDD.

**Configuration initiale :**

| Source | Bonus vitesse ATQ | Durée |
|--------|--------|--------|
| Compétence A | \+5 % | 3 secondes |
| Compétence B | \+3 % | 6 secondes |

**Chronologie des effets**

**0 à 3 secondes** (\+8 %)

Compétence A (+5 %) + Compétence B (+3 %)

---

**3 à 6 secondes** (\+3 %)

Compétence A expirée. Compétence B toujours active.

Mathématiquement :

$$
B_{\text{actif}}(t)=\sum_{i\in A(t)}B_i
$$

Où $A(t)$ représente l'ensemble des instances de bonus actives à l'instant $t$.

### 1.3 Règles techniques complémentaires

Nous distinguons désormais trois notions :

- `source_id` : identifie la compétence, l'équipement ou le système qui produit l'effet.
- `instance_id` : identifie chaque application individuelle de cet effet.
- `stacking_group` : détermine les effets qui se cumulent ensemble.

Les règles sont les suivantes :

1. Deux compétences différentes peuvent cumuler leurs bonus.
2. Les bonus du même groupe sont additionnés.
3. Chaque instance conserve sa propre durée.
4. L'expiration d'une instance ne supprime pas les autres.
5. Une nouvelle application provenant de la même source suit la politique `UNIQUE_SOURCE` si celle-ci est configurée.
6. `HIGHEST`, `LOWEST` et `REPLACE` restent disponibles uniquement pour les effets explicitement conçus avec ces politiques.

**Précision de cohérence :** les bonus appartenant à des groupes indépendants restent multiplicatifs, conformément à SYS-002.D.6.1. Ton exemple concerne deux bonus de vitesse d'attaque appartenant au même groupe additif.

*Note d'ingénierie : une instance d'effet ne sera jamais écrasée par une autre source. Le moteur conservera chaque durée indépendamment. C'est cette séparation qui garantit la restauration correcte des bonus après expiration.*

---

</details>


### SYS-002.D.6.4 · T020 · 18/11/2026 14:35:48

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 5990 · **Ligne de formalisation :** 5995.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.6.4 : résistances négatives = clamp ; dégâts minimum = zero ; arrondi = floor ; application contraintes = final ; dénominateur critique invalide = reject ; observations = Je ne sais plus si j'ai déjà parlé des caractéristiques : Combo d'Acolyte et Coup critique d'Acolyte qui sont également des caractéristiques comme le Combo, la Contre attaque, le Coup critique etc.... Formalise les décisions et poursuis vers la validation globale du Character Stats Engine.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD — SYS-002.D.6.4

(Validé) (Version 1.0)

## 1.1 Décisions enregistrées

| Élément | Décision |
|--------|--------|
| Résistances négatives | Ramener la valeur effective à 0 % |
| Résistance maximale | 100 % |
| Dégâts minimum | 0 |
| Arrondi des dégâts | `floor()` |
| Application des contraintes | Après résolution des modificateurs |
| Dénominateur critique invalide | Rejet de la configuration |

## 1.2 Règles mathématiques

**Résistances :**

$$
R_{\text{effective}}=\operatorname{clamp}(R_{\text{raw}},0,100)
$$

La valeur brute est conservée. Seule la valeur effective est limitée.

**Dégâts appliqués :**

$$
D_{\text{appliqué}}=
\max(0,\lfloor D_{\text{calculé}}\rfloor)
$$

**Résistance critique :**

$$
CR_{\text{défenseur}}>0
$$

Toute configuration ne respectant pas cette contrainte est rejetée.

Les contrôles de sécurité indispensables restent effectués au moment où une valeur est consommée : une probabilité doit être valide avant son tirage aléatoire, et un dénominateur doit être valide avant une division.

---

# 2. Mise à jour du dictionnaire des attributs

## 2.1 Nouveaux attributs : acolytes

Les deux caractéristiques que tu viens de mentionner n'étaient effectivement pas présentes dans notre inventaire initial.

Nous les ajoutons.

| Attribut | Identifiant technique |
|--------|--------|
| Combo d'acolyte | `acolyte_combo_rate` |
| Coup critique d'acolyte | `acolyte_critical_rate` |

(Ajoutés au référentiel)

### Règles de conception

Ces caractéristiques sont indépendantes des attributs généraux :

- `combo_rate`
- `critical_rate`

Elles concernent les attaques provenant des acolytes et ne doivent pas modifier les statistiques du personnage joueur.

Leurs formules précises restent à spécifier.

Nous ne créons pas automatiquement des caractéristiques supplémentaires sans confirmation :

- Ignorance du combo d'acolyte.
- Ignorance du coup critique d'acolyte.
- Dégâts critiques d'acolyte.
- Coefficient de combo d'acolyte.

Ces éléments sont inscrits dans les points à vérifier.

## 2.2 Nouveau bilan du référentiel

# 4

Attributs basiques

# 56

Attributs avancés

# 4

Attributs finaux

---

**Total des définitions**

# 64

Les quatre attributs finaux sont des valeurs dérivées, et non des sources indépendantes de statistiques.

---

# 3. Référentiel consolidé — 56 attributs avancés

Voici la structure complète actuelle.

## 3.1 Déclenchement et mécaniques de combat — 20

| Identifiant | Attribut |
|--------|--------|
| `critical_rate` | Coup critique |
| `critical_ignore` | Ignorance de coup critique |
| `critical_damage` | Dégâts critiques |
| `critical_resistance` | Résistance critique |
| `combo_rate` | Combo |
| `combo_ignore` | Ignorance du combo |
| `counter_attack_rate` | Contre-attaque |
| `counter_attack_ignore` | Ignorance de contre-attaque |
| `stun_rate` | Étourdissement |
| `stun_ignore` | Ignorance d'étourdissement |
| `evasion` | Évasion |
| `evasion_ignore` | Ignorance d'évasion |
| `regeneration_rate` | Régénération |
| `regeneration_ignore` | Ignorance de régénération |
| `airborne_rate` | En vol |
| `airborne_ignore` | Ignorance d'en vol |
| `block_rate` | Blocage |
| `block_ignore` | Ignorance de blocage |
| `acolyte_combo_rate` | Combo d'acolyte |
| `acolyte_critical_rate` | Coup critique d'acolyte |

## 3.2 Coefficients et compétences — 11

| Identifiant | Attribut |
|--------|--------|
| `normal_attack_coefficient` | Coefficient d'ATQ normale |
| `normal_attack_damage_reduction` | Réduction des dégâts d'ATQ normale |
| `combo_coefficient` | Coefficient de combo |
| `combo_damage_reduction` | Réduction des dégâts de combo |
| `counter_attack_coefficient` | Coefficient de contre-attaque |
| `counter_attack_damage_reduction` | Réduction des dégâts de contre-attaque |
| `skill_critical_rate` | Coup critique de compétence |
| `skill_critical_ignore` | Ignorance du coup critique de compétence |
| `skill_critical_damage` | Dégâts critiques de compétence |
| `skill_damage` | Dégâts de compétence |
| `skill_damage_reduction` | Réduction des dégâts de compétence |

## 3.3 Boss et acolytes — 8

| Identifiant | Attribut |
|--------|--------|
| `boss_damage` | Dégâts de boss |
| `boss_damage_reduction` | Réduction des dégâts de boss |
| `acolyte_damage` | Dégâts d'acolyte |
| `acolyte_damage_reduction` | Réduction des dégâts d'acolyte |
| `acolyte_inspiration` | Inspiration des acolytes |
| `acolyte_inspiration_ignore` | Ignorance de l'inspiration des acolytes |
| `acolyte_resistance` | Résistance des acolytes |
| `acolyte_resistance_ignore` | Ignorance de résistance des acolytes |

## 3.4 Guérison — 2

| Identifiant | Attribut |
|--------|--------|
| `healing_rate` | Taux de guérison |
| `healing_amount` | Quantité de guérison |

## 3.5 Pénétration — 8

| Identifiant | Attribut |
|--------|--------|
| `armor_penetration` | Perforation d'armure |
| `armor_penetration_ignore` | Ignorance de perforation d'armure |
| `penetration` | Pénétration |
| `anti_penetration` | Anti-pénétration |
| `skill_penetration` | Pénétration de compétence |
| `skill_anti_penetration` | Anti-pénétration de compétence |
| `acolyte_penetration` | Pénétration d'acolyte |
| `acolyte_anti_penetration` | Anti-pénétration d'acolyte |

## 3.6 Bonus globaux — 7

| Identifiant | Attribut |
|--------|--------|
| `damage_reduction` | Réduction des dégâts |
| `hp_bonus` | Bonus de PV |
| `attack_bonus` | Bonus d'ATQ |
| `defense_bonus` | Bonus de DEF |
| `attack_speed_bonus` | Bonus de vitesse d'ATQ |
| `final_damage_increase` | Augmentation des dégâts finales |
| `final_damage_reduction` | Réduction des dégâts finale |

---

</details>

