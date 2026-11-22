# Chapitre 02 — Défense, pénétration et résistances

**Autorité :** décisions expressément approuvées dans la conversation source. Les modèles obsolètes sont remplacés par les rectifications ultérieures ; les paramètres provisoires restent provisoires.

**Statut du chapitre :** `functionally_specified` pour ses spécifications validées ; aucune exécution de test ou implémentation ne découle de ce statut.

**Traçabilité :** 3 décision(s) du propriétaire. Toutes les références `Txxx` renvoient à `references/HISTORIQUE_SOURCE_ORIGINAL.md`.

## Modèle DEF ratifié

\[
M_{DEF}=\frac{DEF_{eff}}{DEF_{eff}+K},\qquad D_{apres\,DEF}=D_{avant\,DEF}\frac{K}{DEF_{eff}+K}
\]

La constante **K est configurable et en attente de calibration**, sans hypothèse numérique présentée comme définitive. La pénétration et la perforation restent des mécanismes distincts, selon T009–T010.


## Registre détaillé des décisions approuvées


### SYS-002.D.2.1 · T008 · 17/11/2026 18:04:39

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 2076 · **Ligne de formalisation :** 2081.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.2.1 : modèle B. Constante K : dynamic. Précisions : Aucune.. Formalise la décision et poursuis avec la spécification des mécanismes de pénétration et perforation d'armure.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.2.1

(Validé) (Version 1.0)

**Modèle retenu : mitigation à rendement décroissant.**

$$
M_{\text{DEF}}=\frac{DEF_{\text{eff}}}{DEF_{\text{eff}}+K}
$$

$$
D_{\text{reçu}}=D_{\text{brut}}\times(1-M_{\text{DEF}})
$$

| Paramètre | Décision |
|--------|--------|
| Modèle | Rendement décroissant |
| Constante K | À déterminer expérimentalement |
| DEF effective minimale | 0 |
| Mitigation | Calcul en précision flottante |
| Arrondi | À l'application finale des dégâts |
| Plafond de mitigation | Aucun plafond arbitraire à ce stade |

**Précision sur K :** K sera un paramètre configurable, calibré à partir des distributions réelles de DEF observées dans le jeu. Il ne sera pas recalculé arbitrairement à chaque attaque. Sa valeur devra rester cohérente à l'intérieur d'un même contexte de combat.

Cette décision est désormais intégrée au référentiel mathématique.

---

</details>


### SYS-002.D.2.2 · T009 · 17/11/2026 18:19:50

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 2449 · **Ligne de formalisation :** 2454.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.2.2 : modèle DEF = keep ; cumul pénétration = multiplicative ; ajout anti-pénétration compétence = oui ; perforation armure = instant ; observations = Aucune. Formalise les décisions et poursuis selon le protocole de validation.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.2.2

(Validé) (Version 1.0)

## 1.1 Décisions actées

| Élément | Décision |
|--------|--------|
| Modèle de défense | Rendement décroissant |
| Pénétration générale | Cumul multiplicatif |
| Pénétration de compétence | Cumul multiplicatif |
| Pénétration d'acolyte | Cumul multiplicatif |
| Anti-pénétration de compétence | Ajoutée |
| Perforation d'armure | Effet instantané |

## 1.2 Formalisation de la pénétration

Pour chaque catégorie de pénétration :

$$
\Delta P=P_{\text{attaquant}}-AP_{\text{défenseur}}
$$

$$
n=\left\lfloor\frac{|\Delta P|}{1000}\right\rfloor
$$

Le multiplicateur retenu est :

$$
M_P=
\begin{cases}
1.10^n & \text{si }\Delta P>0\\
0.90^n & \text{si }\Delta P<0\\
1 & \text{si }\Delta P=0
\end{cases}
$$

Cette règle reprend les tranches complètes de 1 000 points proposées précédemment. Les valeurs intermédiaires ne produisent pas de tranche supplémentaire.

Trois calculs indépendants seront disponibles :

- `general_penetration_multiplier`
- `skill_penetration_multiplier`
- `acolyte_penetration_multiplier`

Chaque multiplicateur ne s'applique qu'à sa catégorie de dégâts.

## 1.3 Formalisation de la perforation d'armure

La règle de conception retenue est :

1. Calcul de la perforation effective.
2. Vérification du déclenchement à 30 %.
3. Calcul de l'ignorance de résistance.
4. Application immédiate à l'attaque déclenchante.
5. Suppression de l'effet après résolution de cette attaque.

L'effet n'est ni cumulatif ni persistant.

Important : cette dernière règle est désormais une décision de conception de notre version. Elle ne constitue pas une confirmation du comportement exact du jeu officiel.

## 1.4 Mise à jour du référentiel

Ajout :

| Attribut | Identifiant |
|--------|--------|
| Anti-pénétration de compétence | `skill_anti_penetration` |

Le référentiel compte désormais 57 attributs avancés, en conservant les caractéristiques initialement communiquées.

---

# 2. Vérification des mécaniques de référence

La confrontation avec la documentation communautaire de Legend of Mushroom permet de confirmer plusieurs règles importantes.

| Mécanisme | Règle documentée |
|--------|--------|
| Pénétration générale | \+10 % par tranche de 1 000 |
| Anti-pénétration | Multiplicateur ×0,9 par tranche de 1 000 |
| Pénétration de compétence | Même logique, catégorie indépendante |
| Pénétration d'acolyte | Même logique, catégorie indépendante |
| Perforation d'armure | Déclenchement à 30 %, jusqu'à 50 % d'ignorance de résistance |
| Blocage | Déclenchement à 30 %, jusqu'à 50 % de résistance supplémentaire |

\[[Характеристики: базовы...](https://legendofmushroom.ru/books/7-klassy-i-sborki/page/xarakteristiki-bazovye-prodvinutye-povedenie-vo-vremia-boia?utm_source=chatgpt.com); [Обновление от 28.05.2025](https://legendofmushroom.ru/books/2-novosti-i-obnovleniia/page/obnovlenie-ot-28052025?utm_source=chatgpt.com)\]

Deux précisions importantes :

- La perforation d'armure concerne les résistances aux attaques normales, compétences, boss, combos et contre-attaques. Son application aux dégâts d'acolytes n'est pas établie par cette documentation.
- La durée exacte de l'effet de perforation n'est pas documentée. Nous conservons donc ton choix d'application instantanée comme règle propre à notre implémentation.

**Correction du dictionnaire :** la liste initiale contient 53 attributs avancés. Avec l'ajout de l'anti-pénétration de compétence, nous en avons 54, et non 57 comme indiqué précédemment.

---

</details>


### SYS-002.D.2.3 · T010 · 17/11/2026 18:26:12

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 2755 · **Ligne de formalisation :** 2760.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.2.3 : cumul des résistances = multiplicative ; portée perforation armure = specific ; dégâts de boss = separate ; observations = Aucune. Formalise la décision et poursuis vers la prochaine spécification.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.2.3

(Validé) (Version 1.0)

| Élément | Décision retenue |
|--------|--------|
| Cumul des résistances | Multiplicatif |
| Portée de la perforation d'armure | Résistances spécifiques uniquement |
| Dégâts de boss | Modificateur indépendant |
| Réduction globale | Couche indépendante |
| Réduction finale | Couche indépendante |

## 1.1 Formule consolidée

Nous établissons le pipeline suivant :

$$
\begin{aligned}
D_1 &= D_{\text{brut}}\times M_{\text{DEF}}\\
D_2 &= D_1\times M_{\text{pénétration}}\\
D_3 &= D_2\times(1-R_{\text{spécifique,eff}})\\
D_4 &= D_3\times M_{\text{boss}}\\
D_5 &= D_4\times(1-R_{\text{boss}})\\
D_6 &= D_5\times(1-R_{\text{globale}})\\
D_{\text{final}} &= D_6\times(1+B_{\text{final}})\times(1-R_{\text{final}})
\end{aligned}
$$

Où les résistances sont exprimées sous forme décimale.

La perforation d'armure intervient dans le calcul de $R_{\text{spécifique,eff}}$, avant son application.

Les limites, plafonds et interactions entre résistances seront spécifiés dans une étape ultérieure.

*Note d'ingénierie : le moteur conservera chaque couche de calcul séparément. Nous pourrons ainsi tracer précisément l'origine d'une variation de dégâts et tester chaque mécanisme indépendamment.*

---

</details>

