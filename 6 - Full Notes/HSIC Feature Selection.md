2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Selection Connections and Evaluation]]

# HSIC Feature Selection

HSIC feature selection chooses variables whose induced kernel has strong statistical dependence with a target kernel, measured by the Hilbert-Schmidt Independence Criterion. Forward selection or backward elimination can search for a useful subset.

With a linear feature kernel, the objective decomposes into a sum of feature-wise quadratic forms. Each feature is then aligned with a transformed target similarity matrix, making the method a univariate spectral selector. General nonlinear kernels can express richer dependence but require repeated kernel construction and are more expensive.

# References

[[spectralfeatureselectionfordatamining.pdf]]

