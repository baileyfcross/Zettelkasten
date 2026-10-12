2026-09-14 21:00

Status: #baby

Tags: [[Probabilistic Classification Models]]

# Markov Random Field Classification

Markov random field classification uses an undirected graph to encode local conditional independencies. The joint distribution factorizes over cliques through compatibility potentials rather than directed conditional probabilities.

This formulation is useful when relationships are symmetric or no causal ordering is appropriate. Classification requires estimating or approximating the distribution of labels given observations, and cycles can make exact normalization and inference difficult.

# References

[[dataclassification.pdf]]
