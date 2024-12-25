# Genetic Algorithm

This work aims to optimize the hyperparameters of an **MLP** based on the **genetic algorithm**.
The dataset used is simplified **MNIST** (we only took the 0s and 1s).

> To run the program use `python version 3.9.11` you can use the following link to download it [python 3.9.11]()

## Chromosomes

Chromosomes are the potential solutions of a **Genetic Algorithm**, and we seek for optimizing those solutions. In this context, the genes of a chromosome include: ***The number of neurons present in the hidden layer***, ***the learning rate***, ***the regularization parameter (alpha in MLP)***, ***the weights*** and ***the biases***.
The size of the population: 10.

## Fitness Evaluation

Entraînement de MLP, et calcule d'erreur de classification.

## Parents' Selection

We used the **Roulette wheel selection**.

## Arithmetical Crossover

alpha entre 0 et 1.

Enfant1 = alpha x Parent1 + (1 - alpha) x Parent2

Enfant2 = (1 - alpha) x Parent1 + alpha x Parent2

## Termination

We chose *the number of generations* as the termination cretiria.

# Results

* The accuracy after the optimization of the hyperparameters became higher then the accuracy before it. We conclude that the GA is helpful when it comes to choosing the best parameters for the model.
