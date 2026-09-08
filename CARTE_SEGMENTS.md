# Carte des segments RFM — Lumina & Co (TP2, Jour 2)

Base : 49 190 clients avec au moins une vente produit valorisée (sur 50 295 clients au total — 1 105 clients
sans vente valorisée exclus, cf. `TP2_Segmentation_RFM.ipynb`, Étape 1).
Snapshot date : **30 juin 2026**. Détail des calculs, du scoring et des graphiques : voir le notebook.

Priorité de traitement : 1 = à traiter en premier.

---

## 1. À risque — priorité 1
**4 835 clients (9,8 %) · 10,3 % du CA historique**

- **Qui ils sont :** forte valeur passée (fréquence ou montant dans le top 40 %), mais absents depuis longtemps
  (récence médiane 446-750 jours selon la définition retenue).
- **Potentiel :** le plus élevé de tous les segments non-Champions — comportement d'achat déjà prouvé.
- **Risque :** churn silencieux en cours, sans signal explicite.
- **Action :** campagne de réactivation personnalisée (historique produit réel), incitation ciblée
  (livraison offerte, avantage exclusif).
- **Critère de priorité :** ROI de rétention le plus élevé du portefeuille.

## 2. Champions — priorité 2
**10 111 clients (20,6 %) · 64,0 % du CA**

- **Qui ils sont :** achat récent, fréquent, gros montant — le cœur économique de l'entreprise.
- **Potentiel :** déjà maximal individuellement ; le levier est la rétention et le parrainage.
- **Risque :** complaisance côté marque — les négliger les fait glisser vers "À risque".
- **Action :** programme VIP / accès anticipé, pas de remise générique (préserver la marge).
- **Critère de priorité :** valeur actuelle la plus élevée — protéger l'existant prime sur la conquête.

## 3. Nouveaux / Prometteurs — priorité 3
**4 287 clients (8,7 %) · 3,2 % du CA**

- **Qui ils sont :** achat très récent, peu d'historique — trop tôt pour juger la fidélité.
- **Potentiel :** inconnu mais non négatif (signal d'entrée positif).
- **Risque :** perte dès le 2e achat manqué si l'onboarding est faible.
- **Action :** séquence de bienvenue, incitation au 2e achat sous 30-60 jours.
- **Critère de priorité :** fenêtre d'activation la plus courte — agir vite ou les perdre.

## 4. Fidèles — priorité 4
**9 535 clients (19,4 %) · 15,9 % du CA**

- **Qui ils sont :** engagés sur les 3 dimensions sans être au sommet — vivier direct des futurs Champions.
- **Potentiel :** élevé, souvent à un seul cran de "Champions".
- **Risque :** modéré — glissement possible vers "À surveiller" si non nourris.
- **Action :** programme de fidélité à paliers, cross-sell sur catégories non achetées.
- **Critère de priorité :** potentiel de croissance solide mais pas de signal de risque actif.

## 5. Gros paniers occasionnels — priorité 5
**348 clients (0,7 %) · 0,9 % du CA**

- **Qui ils sont :** achats rares mais très chers — probablement en partie des comptes B2B (cf. outliers Jour 1).
- **Potentiel :** élevé par transaction ; le levier est l'upsell, pas la fréquence.
- **Risque :** faible en volume, mais chaque perte individuelle pèse lourd.
- **Action :** contact commercial dédié, à ne pas mélanger aux campagnes de masse.
- **Critère de priorité :** valeur par client élevée mais volume trop faible pour plus de budget.

## 6. À surveiller — priorité 6
**10 089 clients (20,5 %) · 3,8 % du CA**

- **Qui ils sont :** comportement médian partout — le plus gros segment en nombre, le plus flou en profil.
- **Potentiel :** hétérogène par construction (segment "reste").
- **Risque :** dilution du budget marketing si traité comme un bloc homogène.
- **Action :** pas de campagne dédiée à ce stade — à re-découper avec une variable supplémentaire
  (catégorie préférée, canal d'acquisition) avant d'investir.
- **Critère de priorité :** priorité "analyse", pas encore priorité "budget".

## 7. Hibernants — priorité 7
**6 830 clients (13,9 %) · 1,5 % du CA**

- **Qui ils sont :** faibles sur les 3 dimensions, inactifs, mais pas au plancher absolu.
- **Potentiel :** faible.
- **Risque :** faible aussi — il n'y a plus grand-chose à perdre.
- **Action :** communication automatisée à très bas coût uniquement, exclusion des campagnes payantes.
- **Critère de priorité :** valeur et risque tous deux faibles.

## 8. Perdus — priorité 8
**3 155 clients (6,4 %) · 0,3 % du CA**

- **Qui ils sont :** un seul petit achat, ancien, jamais renouvelé.
- **Potentiel :** quasi nul.
- **Risque :** aucun risque de perte de CA — le risque réel est le gaspillage de budget.
- **Action :** exclusion des campagnes payantes, email automatisé sans coût marginal au mieux.
- **Critère de priorité :** aucune valeur récupérable.

---

## Vérification anti-priorisation théorique

Si "À risque" (rang 1) et "Fidèles" (rang 4) recevaient tous deux un simple email générique mensuel, ce
classement ne serait qu'un exercice sur papier. Dans les faits : "À risque" reçoit une campagne **personnalisée
avec incitation financière** (coût par client élevé, ciblage individualisé), "Fidèles" reçoit un **programme de
fidélité automatisé** (coût marginal quasi nul, contenu identique pour tout le segment). L'écart de traitement
reflète l'écart de rang.

## Ce que le croisement zero-party n'apporte pas

Croisé avec `age_bracket`, `declared_preference` et `life_stage` (`customers.csv`), aucun segment RFM ne montre
de sur-représentation démographique ou déclarative significative (écarts de moins de 1,5 point vs. la base
globale). Le signal comportemental (RFM) et le signal déclaratif semblent indépendants sur cette base — le
ciblage des campagnes doit donc rester construit sur l'historique d'achat réel, pas sur le profil démographique
déclaré. Détail du calcul : `TP2_Segmentation_RFM.ipynb`, section "Pour aller plus loin — croisement zero-party".
