2026-09-14 22:06

Status: #baby

Tags: [[C++ Specialized Clustering Implementations]]

# Genetic K-Modes Selection and Mutation

Selection favors fitter K-modes chromosomes for reproduction, crossover recombines their encoded structure, and mutation introduces categorical changes that preserve exploration. The iteration repeats for a configured number of generations.

Strong selection can collapse diversity prematurely, while excessive mutation turns search into noise. Population size, probabilities, seed, and stopping behavior are therefore part of the algorithm's reproducible configuration.

# References

[[dataclusteringincplusplus.pdf]]

