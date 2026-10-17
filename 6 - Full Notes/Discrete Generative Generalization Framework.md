2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Discrete Generative Generalization Framework

For a constrained binary problem, let $S$ be the valid solution space and let the training set contain $T=\epsilon|S|$ examples. A trained generative model is queried to produce samples, which can be classified by whether they were absent from training, satisfy the constraints, and improve an application-defined cost.

This sample-based formulation compares implicit and explicit generative models without requiring access to their exact likelihoods. It refines [[Generalization in Machine Learning]] for unsupervised generation by separating three questions: whether the model leaves the training set, whether its novel outputs are valid, and whether those outputs are useful.

Those questions become [[Generative Pre-Generalization Exploration]], [[Validity-Based Generative Generalization]], and [[Quality-Based Generative Generalization]]. The separation matters because a model can generate many novel strings while violating constraints, or generate valid strings that offer no improvement over training data.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

