# Chapitre 05 — Cadence, vitesse et temps

**Autorité :** décisions expressément approuvées dans la conversation source. Les modèles obsolètes sont remplacés par les rectifications ultérieures ; les paramètres provisoires restent provisoires.

**Statut du chapitre :** `functionally_specified` pour ses spécifications validées ; aucune exécution de test ou implémentation ne découle de ce statut.

**Traçabilité :** 2 décision(s) du propriétaire. Toutes les références `Txxx` renvoient à `references/HISTORIQUE_SOURCE_ORIGINAL.md`.


## Registre détaillé des décisions approuvées


### SYS-002.D.5.1 · T015 · 17/11/2026 20:03:26

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 4147 · **Ligne de formalisation :** 4152.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.5.1 : unité = aps ; portée = basic_skill ; cumul des bonus = hybrid ; plafond = none ; observations = Aucune. Formalise les décisions et poursuis avec la spécification de la cadence, des cooldowns et des modifications de vitesse en combat.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.5.1

(Validé) (Version 1.0)

## 1.1 Décisions enregistrées

| Élément | Décision |
|--------|--------|
| Unité | Attaques par seconde (APS) |
| Portée | Attaques normales et exécution des compétences |
| Cooldowns | Indépendants de la vitesse d'attaque |
| Cumul des bonus | Hybride |
| Plafond maximal | Aucun plafond artificiel |

## 1.2 Calcul de la vitesse finale

La formule architecturale retenue est :

$$
AS_{\text{final}}=AS_{\text{base}}\times\prod_{g=1}^{n}
\left(1+\sum_{j=1}^{m_g}B_{g,j}\right)
$$

Les bonus d'une même catégorie sont additionnés. Les catégories indépendantes sont multipliées.

Les catégories et leur composition seront définies dans le dictionnaire des attributs.

## 1.3 Principes invariants

- La vitesse finale est exprimée en APS.
- Les attaques normales utilisent cette valeur pour déterminer leur cadence.
- Les compétences utilisent cette valeur pour déterminer leur vitesse d'exécution.
- Les cooldowns ne sont pas réduits par la vitesse d'attaque.
- Aucun plafond maximal arbitraire ne sera imposé.
- Une vitesse nulle suspend les attaques normales ; une vitesse négative est invalide.

---

</details>


### SYS-002.D.5.2 · T016 · 17/11/2026 20:17:57

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 4558 · **Ligne de formalisation :** 4563.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.5.2 : première attaque = immediate ; modification dynamique = preserve ; début cooldown = activation ; exécution compétence = inverse ; verrou compétences = parallel ; précision temporelle = microseconds ; observations = Aucune. Formalise les décisions et poursuis selon le protocole.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.5.2

(Validé) (Version 1.0)

## 1.1 Décisions enregistrées

| Élément | Décision |
|--------|--------|
| Première attaque | Immédiate dès que la cible est à portée |
| Modification dynamique | Préservation de la progression du cycle |
| Début du cooldown | Au déclenchement |
| Exécution des compétences | Inversement proportionnelle à la vitesse |
| Exécution simultanée | Plusieurs compétences en parallèle |
| Précision temporelle | Microsecondes entières, 64 bits |

## 1.2 Cadence des attaques

$$
T_{\text{attaque}}=\frac{1\,000\,000}{AS_{\text{final}}}
$$

Le résultat est exprimé en microsecondes.

La première attaque intervient dès que les conditions de combat sont réunies. Les suivantes respectent la cadence calculée.

## 1.3 Modification dynamique de vitesse

La progression temporelle est conservée.

$$
p=\frac{t_{\text{écoulé}}}{T_{\text{cycle}}}
$$

$$
T_{\text{restant}}=(1-p)\times T_{\text{nouveau}}
$$

Cette règle s'applique aux cycles d'attaques et aux exécutions de compétences.

## 1.4 Compétences parallèles

Chaque compétence possède son propre état :

- Temps d'activation.
- Cooldown.
- Durée d'exécution.
- Progression d'exécution.
- État d'exécution.

Plusieurs compétences distinctes peuvent être exécutées simultanément.

Le cooldown commence à l'activation, indépendamment de la fin de l'exécution.

Une règle complémentaire reste à définir : une même compétence pourra-t-elle être relancée alors que son exécution précédente n'est pas terminée ? Je propose de l'interdire par défaut, sans empêcher l'exécution parallèle de compétences différentes.

## 1.5 Précision temporelle

Le moteur utilisera :

- `int64` pour les timestamps.
- Des microsecondes comme unité interne.
- Un accumulateur pour les intervalles fractionnaires.
- Un ordonnancement déterministe des événements.

---

</details>

