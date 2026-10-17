2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Generative Quality Coverage

Quality coverage measures the diversity of improvements produced by a generative model. It counts the unique, valid, unseen samples whose cost is lower than the best cost in the training set, then divides that count by the number $Q$ of generated queries.

Unlike [[Generative Quality Minimum and Utility]], quality coverage rewards finding many different useful candidates rather than concentrating probability on a few strong outputs. It therefore exposes mode collapse and repeated sampling that a best-value statistic can miss.

The threshold is relative to the training data rather than to a known global optimum. A model can achieve nonzero quality coverage by improving a weak training set without solving the full optimization problem, so the training set's minimum cost must be controlled when comparing data regimes.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

