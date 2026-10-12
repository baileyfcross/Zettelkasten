2026-09-14 21:00

Status: #baby

Tags: [[Probabilistic Classification Models]]

# Bayesian Network Inference

Bayesian network inference computes the probability of unobserved variables after evidence is fixed on observed nodes. For classification, the central query is the posterior distribution of the class variable.

The graph's factorization avoids manipulating a fully enumerated joint table, but exact inference can still become expensive when dependencies create large intermediate factors. Approximate procedures trade exactness for tractability in densely connected structures.

A directed dependency can encode the generative direction from a hidden cause to an observed symptom, while diagnosis asks for the probability in the opposite direction. Conditional probability and Bayesian inversion let evidence about the symptom update belief in the cause without reversing the assumed causal mechanism itself.

# References

[[dataclassification.pdf]]

[[machinelearning_mit.epub]]
