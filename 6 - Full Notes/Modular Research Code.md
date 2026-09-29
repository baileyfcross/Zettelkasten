2026-09-28 21:33

Status: #baby

Tags: [[Reproducible Scientific Software]]

# Modular Research Code

Modular research code separates a large analysis into components with explicit inputs, outputs, and limited responsibilities. A module can be tested or replaced without requiring the whole project to be understood at once.

For long-running work, modularity also creates natural checkpoints for [[Dependency-Aware Research Execution]] and saved intermediate results. The boundaries should follow scientific operations rather than arbitrary file sizes. When responsibilities become clearer during development, [[Research Code Refactoring]] can improve the structure while [[Unit Test|unit tests]] protect established behavior.

# References

[[implementingreproducableresearch.pdf]]
