2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Maximally Entangled Copula Marginals

For two equal variable registers $A$ and $B$, the copula circuit begins with $2^{-n/4}\sum_i |i\rangle_A|i\rangle_B$. Its reduced density matrix on either register is proportional to the identity, so measuring that register alone gives the discrete uniform distribution.

The trainable circuit has the separable form $U_A\otimes U_B$ after this initialization. Local unitaries preserve the Schmidt coefficients and therefore keep each reduced state maximally mixed even while changing the correlations between paired outcomes.

Uniformity is consequently an invariant of the circuit rather than a penalty that training must learn. The benefit is a strong inductive bias for copula data; the cost is that the same architecture cannot represent arbitrary nonuniform marginals without an external inverse transform.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

