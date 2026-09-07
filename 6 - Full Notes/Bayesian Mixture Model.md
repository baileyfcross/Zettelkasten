2026-09-06 21:47

Status: #baby

Tags: [[Probabilistic Model Composition]]

# Bayesian Mixture Model

A Bayesian mixture model introduces a hidden choice variable whose values identify component models. Conditioned on one choice, the data follows the corresponding component distribution; marginalizing the choice produces a weighted sum of the components.

The weights are the probabilities assigned to the hidden variable and may themselves depend on observed inputs. Retaining the choice variable also allows model recognition by inferring which component best explains the evidence.

# References

[[bayesianprogramming.pdf]]
