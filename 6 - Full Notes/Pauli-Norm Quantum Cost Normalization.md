2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Pauli-Norm Quantum Cost Normalization

For a Hamiltonian $H=\sum_j\alpha_jP_j$, its Pauli coefficient norm is $\lVert H\rVert_*=\sum_j|\alpha_j|$. Dividing the measured expectation by this norm gives the normalized objective

$$\widetilde f(\theta)=\frac{\langle H\rangle_{\theta}}{\lVert H\rVert_*}.$$

Because every Pauli observable has eigenvalues in $\{-1,1\}$, the normalized cost lies within $[-1,1]$. The learned optimizer can therefore receive inputs on a common numerical scale even when Hamiltonian sizes and coefficient magnitudes differ across training instances.

The transformation standardizes the signal but does not remove the physical cost of estimating it. The coefficient norm also enters an upper bound on the number of circuit repetitions needed for a chosen estimation precision.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

