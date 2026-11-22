# Chapitre 03 — Critiques et dégâts critiques

**Autorité :** décisions expressément approuvées dans la conversation source. Les modèles obsolètes sont remplacés par les rectifications ultérieures ; les paramètres provisoires restent provisoires.

**Statut du chapitre :** `functionally_specified` pour ses spécifications validées ; aucune exécution de test ou implémentation ne découle de ce statut.

**Traçabilité :** 2 décision(s) du propriétaire. Toutes les références `Txxx` renvoient à `references/HISTORIQUE_SOURCE_ORIGINAL.md`.


## Registre détaillé des décisions approuvées


### SYS-002.D.3.1 · T011 · 17/11/2026 18:31:16

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 3025 · **Ligne de formalisation :** 3030.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.3.1 : critique général = subtract ; critique compétence = separate ; plafond = 100 ; héritage du type de dégâts = type ; observations = Aucune. Formalise les décisions et poursuis vers SYS-002.D.3.2.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.3.1

(Validé) (Version 1.0)

## 1.1 Décisions enregistrées

| Élément | Décision |
|--------|--------|
| Critique général | Soustraction des attributs antagonistes |
| Critique de compétence | Système indépendant |
| Plafond du taux critique | 100 % |
| Compétence avec type de dégâts spécifique | Hérite du système critique de son type |
| Plancher du taux critique | 0 % |

## 1.2 Formules validées

**Critique général**

$$
P_{\text{crit}}=
\operatorname{clamp}(CR-ICR,0,100)
$$

**Critique de compétence**

$$
P_{\text{skill}}=
\operatorname{clamp}(SCR-ISCR,0,100)
$$

Les valeurs sont exprimées en pourcentage dans le GDD et normalisées entre 0 et 1 dans le moteur.

## 1.3 Règle de sélection du système critique

| Type de dégâts | Système critique |
|--------|--------|
| Attaque normale | Général |
| Combo | Général |
| Contre-attaque | Général |
| Compétence classique | Compétence |
| Compétence infligeant des dégâts de combo | Général |
| Compétence infligeant des dégâts de contre-attaque | Général |

Une attaque ne pourra déclencher qu'un seul calcul critique par impact.

---

# 2. Analyse des mécaniques critiques du jeu de référence

Avant de fixer les formules, j'ai confronté les attributs à plusieurs documentations spécialisées de Legend of Mushroom.

Une distinction importante apparaît :

**La résistance critique ne réduit pas le taux de déclenchement critique. Elle intervient dans le calcul des dégâts critiques.**

Il faut donc distinguer trois mécanismes :

| Mécanisme | Attributs |
|--------|--------|
| Probabilité de critique | Coup critique / Ignorance de coup critique |
| Puissance du critique | Dégâts critiques / Résistance critique |
| Critique de compétence | Critique compétence / Ignorance critique compétence / Dégâts critiques compétence |

Cette distinction est cohérente avec les formules documentées du jeu. \[[LegendOfMushroom.gg :: Your source for Legend of Mushroom guides, tools, and content\!](https://legendofmushroom.gg/guides/how-your-damage-is-actually-calculated?utm_source=chatgpt.com); [Характеристики: базовы...](https://legendofmushroom.ru/books/7-klassy-i-sborki/page/xarakteristiki-bazovye-prodvinutye-povedenie-vo-vremia-boia?utm_source=chatgpt.com)\]

</details>


### SYS-002.D.3.2 · T012 · 17/11/2026 18:36:21

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 3303 · **Ligne de formalisation :** 3308.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.3.2 : dégâts critiques généraux = reference ; dégâts critiques compétence = power ; portée résistance critique = general ; multiplicateur minimal = 150 ; ordre application = before_final ; observations = Aucune. Formalise les décisions et poursuis selon le protocole.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.3.2

(Validé) (Version 1.0)

## 1.1 Décisions enregistrées

| Élément | Décision |
|--------|--------|
| Dégâts critiques généraux | Formule de référence |
| Dégâts critiques de compétence | Formule avec puissance 0,98 |
| Résistance critique | S'applique aux critiques généraux |
| Multiplicateur critique minimal | 1,5 |
| Ordre d'application | Après résistances spécifiques, avant modificateurs finaux |

## 1.2 Formules validées

**Critiques généraux**

$$
M_{\text{crit}}=
\max\left(1.5,\frac{CD}{CR_{\text{défenseur}}}\right)
$$

**Critiques de compétence**

$$
M_{\text{skill crit}}=
\left(1+\frac{SCD}{100}\right)^{0.98}
$$

Ces formules seront conservées dans le GDD comme règles de référence. La convention exacte des unités et valeurs affichées devra être vérifiée avant implémentation.

## 1.3 Ordre de résolution

Le pipeline est désormais :

1. Calcul des dégâts bruts.
2. Mitigation par la défense.
3. Application de la pénétration.
4. Application des résistances spécifiques.
5. Détermination du critique.
6. Application du multiplicateur critique.
7. Application des modificateurs finaux.
8. Arrondi et application des dégâts.

Une attaque ne peut bénéficier que d'un seul système critique par impact.

---

</details>

