2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Scoring and Graph Structure]]

# Spectral Feature Selection Robustness

Spectral feature selection is robust when small perturbations of feature values or the graph Laplacian cause only small changes in feature scores and rankings. Perturbation bounds separate three influences: the size of the matrix perturbation, the size of the feature-vector perturbation, and the eigengaps governing eigenvector stability.

Robustness can improve by excluding tail eigenpairs, whose small gaps and fine-scale patterns often reflect noise, or by using a [[Spectral Matrix Function]] that increases the score separation between relevant and irrelevant features. Aggressive truncation still risks removing real fine-scale structure, so the cutoff must reflect the problem.

# References

[[spectralfeatureselectionfordatamining.pdf]]

