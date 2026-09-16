2026-09-16 01:28

Status: #baby

Tags: [[Streaming Feature Engineering]]

# Online Principal Component Analysis

Online principal component analysis updates a low-dimensional linear subspace as new observations arrive. Incremental updates avoid retaining the full data matrix or recomputing an eigendecomposition from scratch.

The method seeks the dominant variance directions available at the current time. Step sizes, numerical stability, changing distributions, and the number of retained components determine how closely the online representation follows a batch solution.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]
