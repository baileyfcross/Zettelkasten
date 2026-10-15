2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Image-Reconstruction Photon Scaling

A conventional coherent-light imaging pipeline must collect enough photons across every detector cell to estimate an $N$-pixel image at a chosen signal-to-noise level. Under Poissonian shot noise, fixed average brightness, and fixed reconstruction variance, the total photon requirement grows linearly with $N$. The image is then passed to a classical neuron whose dot product also requires $N$ multiply-and-accumulate contributions.

The paper further derives a linear-in-$N$ lower bound for propagating pixel uncertainty through a sigmoid neuron, assuming a nontrivial sequence of learned weights, bounded bias and $\ell_1$ norm, and negligible spatial-neighborhood correlations. These assumptions matter: the bound characterizes a reconstruct-then-classify route under a specific noise and regularity model. [[Bucket-Detector Classification Without Image Reconstruction]] avoids that route by estimating only a task-specific overlap statistic.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
