# Chapitre 01 — Modèle mathématique — dégâts bruts

**Autorité :** décisions expressément approuvées dans la conversation source. Les modèles obsolètes sont remplacés par les rectifications ultérieures ; les paramètres provisoires restent provisoires.

**Statut du chapitre :** `functionally_specified` pour ses spécifications validées ; aucune exécution de test ou implémentation ne découle de ce statut.

**Traçabilité :** 2 décision(s) du propriétaire. Toutes les références `Txxx` renvoient à `references/HISTORIQUE_SOURCE_ORIGINAL.md`.

## Formule fondamentale ratifiée — modèle hybride

\[
D_{brut}=A\times C\times(1+B)\times\prod_{i=1}^{n}M_i
\]

- **A :** attaque finale ; **C :** coefficient de l'action ; **B :** somme des bonus additifs du groupe concerné ; **Mᵢ :** multiplicateurs indépendants.
- L'arrondi n'intervient pas dans les étapes intermédiaires (T007). Le quantificateur final et les restrictions ont été affinés dans T020 et D.13.4.


## Registre détaillé des décisions approuvées


### SYS-002.D.1 · T006 · 17/11/2026 17:16:39

**Nature :** `EXIGENCE_OU_RECTIFICATION_PROPRIETAIRE` · **Ligne d’approbation source :** 1509 · **Ligne de formalisation :** 1515.

**Décision / prescription originale (texte intégral du propriétaire) :**

Continuons.
Pour chaque étape, donnes moi la possibilité de valider les choix afin d'apporter une modification/spécification si necessaire.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

## SYS-002.D.1 — Construction des dégâts bruts

### 1. Objectif

Définir comment le moteur calcule les dégâts théoriques d'une attaque avant toute intervention de la défense adverse, des coups critiques ou des boucliers.

Nous allons distinguer quatre variables :

| Variable | Description |
|--------|--------|
| $A$ | Attaque finale de l'attaquant |
| $C$ | Coefficient de puissance de l'action |
| $B$ | Bonus de dégâts additifs |
| $M$ | Multiplicateurs indépendants |

L'attaque finale $A$ sera fournie par le système de statistiques du personnage. Elle intégrera les caractéristiques de base et les bonus permanents.

### 2. Trois modèles envisageables

**Modèle A — Cumul entièrement additif**

Tous les bonus en pourcentage sont additionnés.

$$
D_{\text{brut}}=A\times C\times(1+\sum b_i)
$$

Avantages :

- Simple à comprendre.
- Facile à équilibrer.
- Limite la croissance exponentielle des dégâts.

Inconvénient : difficile de différencier certains effets spéciaux des bonus classiques.

**Modèle B — Modèle hybride**

Les bonus classiques sont additionnés, tandis que les multiplicateurs spécifiques sont multipliés entre eux.

$$
D_{\text{brut}} =
A\times C\times(1+B)\times\prod M_i
$$

Exemple :

- Attaque : 100.
- Coefficient de compétence : 1,5.
- Bonus équipement : +20 %.
- Bonus passif : +10 %.
- Multiplicateur spécial : ×1,25.

$$
D=100\times1,5\times1,30\times1,25
$$

(243,75 dégâts)

Avantages :

- Bonne flexibilité.
- Distinction claire entre bonus classiques et effets spéciaux.
- Équilibrage indépendant des différentes catégories.
- Architecture extensible.

Inconvénient : nécessite de catégoriser rigoureusement les bonus.

**Modèle C — Cumul entièrement multiplicatif**

Chaque bonus est appliqué indépendamment.

$$
D_{\text{brut}}=A\times C\times\prod(1+b_i)
$$

Avantages :

- Grande liberté dans la conception des bonus.
- Forte progression de puissance.

Inconvénient : croissance potentiellement excessive des dégâts lorsque les bonus deviennent nombreux.

### 3. Ma recommandation

Je recommande le **modèle B : hybride**.

Il permet notamment de distinguer :

- Les bonus permanents provenant de l'équipement.
- Les bonus passifs des compétences.
- Les bonus temporaires.
- Les multiplicateurs spécifiques à certaines attaques.

Nous pourrons également modifier individuellement chaque catégorie sans devoir réécrire le calculateur de dégâts.

*Note d'ingénierie : aucun arrondi intermédiaire ne sera effectué. Le moteur conservera une précision flottante pendant toute la résolution de l'attaque. L'arrondi interviendra au moment de l'application finale des dégâts.*

---

## 4. Validation de SYS-002.D.1

**Quel modèle souhaites-tu retenir ?**

**A — Entièrement additif**

Progression contrôlée et calcul simple.

**B — Hybride (recommandé)**

Bonus additifs et multiplicateurs indépendants.

**C — Entièrement multiplicatif**

Progression de puissance plus agressive.

---

**Modifications ou précisions éventuelles**

[Texte de substitution de la zone de texte : Précise ici les modifications souhaitées. Tu peux également laisser ce champ vide.] (valeur actuelle indisponible.)

[Valider SYS-002.D.1]

**Règle :** nous ne passerons à SYS-002.D.2 (mitigation par la défense) qu'après validation de cette première spécification.

</details>


### SYS-002.D.1 · T007 · 17/11/2026 17:54:18

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 1694 · **Ligne de formalisation :** 1706.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.1 : modèle B. Précisions et modifications : Le mode hybride est très bien.
Je vais rajouter des caractéristiques propres au jeu officiel afin qu'on puisse être sur les mêmes bases.
Attributs basiques :
PV, ATQ,  DEF, Vitesse d'ATQ
Attributs avancés : 
Coup critique, Ignorance de coup critique, Dégâts critique, Résistance critique, Combo, Ignorance du combo, Contre attaque, Ignorance de contre attaque, Etourdissement, Ignorance d'étourdissement, Evasion, Ignorance d'évasion, Régénération, Ignorance de régénération, En vol, Ignorance d'en vol, Coefficient d'ATQ normale, Réduction des dégâts d'ATQ normale, Coefficient de combo, Réduction des dégâts de combo, Coefficient de contre attaque, Réduction des dégâts de contre attaque, Coup critique de compétence, Ignorance du coup critique de compétence, Dégâts critiques de compétence, Dégâts de compétence, Réduction des dégâts de compétence, Dégâts de boss, Réduction des dégâts de boss, Dégâts d'Acolyte, Réduction des dégâts d'acolyte, Taux de guérison, Quantité de guérison, Perforation d'armure, Ignorance de perforation d'armure, Blocage, ignorance de blocage, Inspiration des acolytes, Ignorance de l'inspiration des Acolytes, Résistance des Acolytes, Ignorance de résistance des acolytes, Pénétration, Anti pénétration, Pénétration de compétence, Pénétration d'acolyte, Anti pénétration d'acolyte, Réduction des dégâts, Bonus de PV, Bonus d'ATQ, Bonus de Def, Bonus de vitesse d'ATQ, Augmentation des dégâts finales, Réduction des dégâts finale
Attributs finaux :
PV finaux, ATQ finale, DEF finale, Vitesse d'ATQ finale. Formalise la décision dans le GDD et passe à SYS-002.D.2.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.1

(Validé) (Version 1.1)

**Modèle mathématique retenu : hybride.**

$$
D_{\text{brut}} =
A \times C \times (1+B) \times \prod_{i=1}^{n}M_i
$$

Avec :

- $A$ : attaque finale.
- $C$ : coefficient de l'action.
- $B$ : somme des bonus additifs applicables.
- $M_i$ : multiplicateurs indépendants applicables.

Les bonus seront classés par catégories afin d'éviter les cumuls involontaires.

## 1.1 Référentiel des attributs

Nous introduisons trois niveaux de caractéristiques.

### A. Attributs basiques

| Attribut | Identifiant technique |
|--------|--------|
| PV | `hp` |
| ATQ | `attack` |
| DEF | `defense` |
| Vitesse d'ATQ | `attack_speed` |

### B. Attributs avancés

Je les organise en familles fonctionnelles. Les noms français constituent les libellés de référence.

**Famille 1 - Critiques**

- Coup critique
- Ignorance de coup critique
- Dégâts critique
- Résistance critique
- Coup critique de compétence
- Ignorance du coup critique de compétence
- Dégâts critiques de compétence

**Famille 2 - Mécaniques de combat**

- Combo
- Ignorance du combo
- Contre-attaque
- Ignorance de contre-attaque
- Étourdissement
- Ignorance d'étourdissement
- Évasion
- Ignorance d'évasion
- Régénération
- Ignorance de régénération
- En vol
- Ignorance d'en vol
- Blocage
- Ignorance de blocage

**Famille 3 - Attaques et coefficients**

- Coefficient d'ATQ normale
- Réduction des dégâts d'ATQ normale
- Coefficient de combo
- Réduction des dégâts de combo
- Coefficient de contre-attaque
- Réduction des dégâts de contre-attaque

**Famille 4 - Compétences**

- Dégâts de compétence
- Réduction des dégâts de compétence
- Pénétration de compétence

**Famille 5 - Boss et acolytes**

- Dégâts de boss
- Réduction des dégâts de boss
- Dégâts d'acolyte
- Réduction des dégâts d'acolyte
- Inspiration des acolytes
- Ignorance de l'inspiration des acolytes
- Résistance des acolytes
- Ignorance de résistance des acolytes
- Pénétration d'acolyte
- Anti-pénétration d'acolyte

**Famille 6 - Guérison**

- Taux de guérison
- Quantité de guérison

**Famille 7 - Défense et pénétration**

- Perforation d'armure
- Ignorance de perforation d'armure
- Pénétration
- Anti-pénétration

**Famille 8 - Bonus globaux**

- Réduction des dégâts
- Bonus de PV
- Bonus d'ATQ
- Bonus de DEF
- Bonus de vitesse d'ATQ
- Augmentation des dégâts finales
- Réduction des dégâts finale

### C. Attributs finaux

Ce sont les caractéristiques effectivement exploitées par les systèmes de combat.

| Attribut | Identifiant technique |
|--------|--------|
| PV finaux | `final_hp` |
| ATQ finale | `final_attack` |
| DEF finale | `final_defense` |
| Vitesse d'ATQ finale | `final_attack_speed` |

**Règle architecturale :** les attributs finaux sont calculés à partir des attributs basiques et avancés. Ils ne constituent pas une seconde source de vérité.

## 1.2 Conséquence sur l'architecture

Nous introduisons un nouveau module dans le projet :

`Character Stats Engine`

Sa responsabilité sera de :

- Centraliser les caractéristiques.
- Appliquer les bonus et malus.
- Gérer les interactions entre attributs.
- Calculer les quatre attributs finaux.
- Fournir un résultat cohérent aux autres systèmes.

Nous ne coderons pas individuellement les calculs de statistiques dans les différents modules.

*Note d'ingénierie : chaque attribut disposera de métadonnées précisant son unité, sa catégorie, son périmètre d'application et ses éventuelles limites. Cela évitera notamment de confondre un taux de déclenchement avec un multiplicateur de dégâts.*

---

</details>

