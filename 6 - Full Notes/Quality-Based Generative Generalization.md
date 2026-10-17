2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Quality-Based Generative Generalization

Quality-based generalization evaluates whether a model generates unseen, valid solutions whose application cost is better than the examples used for training. It is especially relevant when generation supports combinatorial optimization, molecule design, or another task in which each candidate can be scored.

The framework uses three complementary quantities. [[Generative Quality Minimum and Utility]] measure the best cost and the average among the best tail of generated solutions, while [[Generative Quality Coverage]] measures how many distinct improvements the model discovers.

No single quantity is sufficient. A very low minimum may be a lucky outlier, a good utility can hide low diversity, and broad coverage can consist of only modest improvements. A practical comparison should report all three under a resource budget fixed before model selection.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

