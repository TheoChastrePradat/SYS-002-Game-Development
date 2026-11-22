# Chapitre 04 — Évasion et probabilités de toucher

**Autorité :** décisions expressément approuvées dans la conversation source. Les modèles obsolètes sont remplacés par les rectifications ultérieures ; les paramètres provisoires restent provisoires.

**Statut du chapitre :** `functionally_specified` pour ses spécifications validées ; aucune exécution de test ou implémentation ne découle de ce statut.

**Traçabilité :** 2 décision(s) du propriétaire. Toutes les références `Txxx` renvoient à `references/HISTORIQUE_SOURCE_ORIGINAL.md`.


## Registre détaillé des décisions approuvées


### SYS-002.D.4.1 · T013 · 17/11/2026 18:49:38

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 3614 · **Ligne de formalisation :** 3622.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.4.1 : formule évasion = reference  plafond = 100 ; précision = remove ; effets après esquive = on_hit ; observations = Il faudrait vérifier comment fonctionne l'évasion dans le jeu officiel.
La définition de l'évasion dans le jeu est : Chance d'esquiver l'ATQ normale lors de l'ATQ normale subit.
Concernant l'ignorance de l'évasion : Réduit le taux d'évasion lors de l'ATQ normale.
Dans le jeu officiel, le taux de l'évasion va au-delà de 100%.. Formalise les décisions dans le GDD et poursuis selon le protocole.


**Source technique :** réponse consécutive et proposition précédant cette validation, consultables dans l’historique original. Aucun extrait automatique n’a été retenu faute de délimitation non ambiguë.


### SYS-002.D.4.2 · T014 · 17/11/2026 19:53:53

**Nature :** `APPROBATION_EXPLICITE` · **Ligne d’approbation source :** 3873 · **Ligne de formalisation :** 3878.

**Décision / prescription originale (texte intégral du propriétaire) :**

Validation SYS-002.D.4.2 : portée = expanded ; plafond PvE = 100 ; plafond PvP = 80 ; formule = reference ; observations = Aucune. Formalise les décisions et poursuis selon le protocole.


<details><summary>Formalisation technique de la décision ratifiée (extrait sourcé)</summary>

# 1. Formalisation GDD - SYS-002.D.4.2

(Validé) (Version 1.0)

## 1.1 Décisions enregistrées

| Élément | Décision |
|--------|--------|
| Portée de l'évasion | Attaques normales, combos, contre-attaques et acolytes |
| Plafond effectif PvE | 100 % |
| Plafond effectif PvP | 80 % |
| Formule | Référence, puissance 0,9 |
| Statistique brute | Peut dépasser 100 % |
| Précision | Non utilisée |

## 1.2 Formule consolidée

$$
E_{\text{net}}=\max(0,E-IE)
$$

$$
E_{\text{effective}}=
\min(E_{\text{net}}^{0.9},E_{\text{cap}})
$$

Avec :

- $E$ : évasion brute du défenseur.
- $IE$ : ignorance d'évasion de l'attaquant.
- $E_{\text{cap}}$ : plafond applicable au mode de jeu.

Les valeurs sont exprimées en points de pourcentage pour cette formule.

| Mode | Plafond effectif |
|--------|--------|
| PvE | 100 % |
| PvP | 80 % |

La statistique brute ne sera jamais écrasée par les calculs intermédiaires.

## 1.3 Contrat technique

Le `EvasionSystem` devra recevoir :

- Les statistiques de l'attaquant.
- Les statistiques du défenseur.
- Le type d'attaque.
- Le mode de jeu.
- Le générateur aléatoire.

Il retournera un `EvasionResult` comprenant la probabilité calculée et le résultat du tirage.

Une attaque esquivée ne déclenche pas les effets nécessitant un impact.

*Note d'ingénierie : les règles PvP sont conservées dans la configuration du mode de jeu, même si le PvP n'est pas prévu dans notre première version. Cela évite de coupler les règles de combat à l'interface ou à la plateforme.*

---

</details>

