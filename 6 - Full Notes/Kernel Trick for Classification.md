2026-09-14 21:00

Status: #baby

Tags: [[Support Vector Classification]]

# Kernel Trick for Classification

The kernel trick replaces an inner product between explicit feature vectors with a kernel function equal to an inner product in an implicit transformed space. A linear separator in that space can represent a nonlinear boundary in the original variables.

This avoids constructing every transformed coordinate, but prediction must evaluate the kernel against support vectors. Kernel choice and its parameters determine the geometry in which margin maximization occurs.

In a reproducing kernel Hilbert space, regularized empirical-risk minimization has a solution in the span of kernel sections centered at the training observations. The support-vector representation is therefore a consequence of the function-space optimization, not merely a numerical shortcut.

# References

[[dataclassification.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
