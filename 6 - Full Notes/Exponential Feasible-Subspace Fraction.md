2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# Exponential Feasible-Subspace Fraction

In one-hot $\kappa$-coloring of $n$ vertices, the feasible subspace has dimension $\kappa^n$, because each vertex has $\kappa$ valid colors. The full $n\kappa$-qubit Hilbert space has dimension $2^{n\kappa}$, so

$$
\frac{\dim \mathcal H_{\mathrm{feasible}}}{\dim \mathcal H}
=\left(\frac{\kappa}{2^\kappa}\right)^n.
$$

For $\kappa>1$, the feasible fraction shrinks exponentially with graph size. A constraint-preserving mixer prevents amplitude from being spent in the exponentially dominant invalid space, though it may require a more costly circuit.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

