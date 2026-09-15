2026-09-14 21:00

Status: #baby

Tags: [[Probabilistic Classification Models]]

# Maximum-Likelihood Naive Bayes Estimation

Maximum-likelihood naive Bayes estimation fits class priors and class-conditional feature parameters from their observed frequencies or sufficient statistics in labeled training data. Conditional independence lets each feature distribution be estimated separately.

The resulting estimates are simple and scalable, but an unseen feature-class combination can receive zero probability and cancel an entire posterior product. Smoothing replaces brittle zero counts with small supported probabilities.

# References

[[dataclassification.pdf]]
