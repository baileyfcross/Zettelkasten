2026-09-29 19:17

Status: #baby

Tags: [[Statistical Learning and Validation]]

# Classifier Dictionary Selection

Classifier dictionary selection chooses among nested or competing hypothesis classes rather than assuming one fixed class. Each dictionary offers a different balance between approximating the Bayes classifier and controlling estimation error.

A penalized empirical-risk criterion can compare these balances, with a complexity term that grows with the dictionary's richness. The procedure exposes why classification is not truly model-free: even under only an i.i.d. assumption, the chosen dictionary encodes beliefs about useful decision boundaries. Poor dictionaries create unavoidable [[Excess Classification Risk]].

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
