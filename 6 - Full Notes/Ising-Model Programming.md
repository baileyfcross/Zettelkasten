2026-09-13 20:16

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# Ising-Model Programming

Ising-model programming expresses a problem through variables and interaction coefficients whose energy is minimized by a desirable solution. On a quantum annealer, execution consists of loading those coefficients, allowing the system to evolve, and reading its qubits.

This workflow can feel unfamiliar to programmers trained in control flow. The central design act is the mathematical encoding that connects a domain problem to the machine’s energy states.

For a two-local model, programming chooses real local biases $h_i$ and pairwise couplings $J_{ij}$ in

$$
\mathcal H(\sigma)=\sum_i h_i\sigma_i+\sum_{i<j}J_{ij}\sigma_i\sigma_j,
\qquad \sigma_i\in\{-1,+1\}.
$$

Correctness means that the desired assignments occupy the minimum-energy set, while undesirable assignments lie higher. Multiple constraint terms can be added, but incompatible minima produce a [[Frustrated Ising Constraint System]] rather than a special “no solution” response.

# References

[[computationalthinking.epub]]
[[Introduction to Quantum Computing-NASA.pdf]]
