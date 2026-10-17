2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# 2-Local Ising Optimization Objective

A two-local Ising objective contains only individual spin biases and pairwise spin couplings:

$$
\mathcal H(\sigma)=\sum_i h_i\sigma_i+\sum_{i<j}J_{ij}\sigma_i\sigma_j,
\qquad \sigma_i\in\{-1,+1\}.
$$

Programming selects $h_i$ and $J_{ij}$ so that low-energy spin assignments correspond to good solutions. The “two-local” restriction means no term directly multiplies three or more decision variables, so higher-order logical relationships must be reduced, canceled, or represented with auxiliary variables before they fit the model.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

