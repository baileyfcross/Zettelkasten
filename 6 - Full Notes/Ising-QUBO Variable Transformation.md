2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# Ising-QUBO Variable Transformation

Ising spins and QUBO bits encode the same binary choice with different alphabets. The linear substitutions

$$
x_i=\frac{\sigma_i+1}{2},
\qquad
\sigma_i=2x_i-1
$$

convert between $x_i\in\{0,1\}$ and $\sigma_i\in\{-1,+1\}$.

Substituting these expressions transforms linear and pairwise coefficients and may add a constant energy offset. The minimizing assignments remain equivalent after decoding. Some constraints are easier to derive in one notation, so conversion allows formulation convenience without changing the underlying discrete problem.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

