# Genetic Algorithm

L'objectif de ce travaille est d'amélioré les hypermaramètre d'un **MLP** en utilisant **l'Algorithme Génétique**.

Le jeu de données utilisé est **MNIST** siplifier (*on a pris juste les 0s et les 1s*)

## La population initiale

La population initiale est une solution d'une **Algorithme Génétique**, et on vise à optimisé cette solution. Dans ce cas, les gènes d'un chromosome sont: ***Le nombre de Neurones dans la couche cachée***, ***Le taux d'apprentissage***, ***Les paramètres de régularisation (alpha dans MLP)***, ***Les poids*** et ***les biais***.

La taille de population dépends de nombre de neurones dans la couche d'antrées.

## Évaluation (fitness)

Entraînement de MLP, et calcule d'erreur de classification.

## Séléction

La méthode de **Roulette** est choisi pour le séléction.

## Critères d'arrêt

Nombre de génération.

## Croisement Arithmétique

alpha entre 0 et 1.

Enfant1 = alpha x Parent1 + (1 - alpha) x Parent2

Enfant2 = (1 - alpha) x Parent1 + alpha x Parent2

# Notes

* The number of generations affect the work of the genetic algorithm, a big number can lead to its divergence. Précision du MLP optimisé par AG: 0.9976 avec un nombre de génération = 50.

# Results

* [ ] Affichez les meilleurs hyperparamètres et leur erreur associée pour chaque génération.
* [ ] Visualisez l'évolution de l'erreur minimale de classification.
* [ ] Graphique montrant l'évolution de la précision
* [ ] Comparer et discuter les résultats obtenus par MLP seul puis MLP optimisé par AG.
