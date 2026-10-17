2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# MaxCut Ising Encoding

MaxCut assigns each graph vertex a spin indicating one of two partitions and rewards adjacent vertices for taking opposite signs. With no local fields, a simple problem Hamiltonian is

$$
\mathcal H(\sigma)=\sum_{(i,j)\in E}\sigma_i\sigma_j.
$$

An edge contributes $-1$ when its endpoints are separated and $+1$ when they remain together, so minimizing the sum maximizes the number of cut edges.

Odd cycles make all pairwise inequality preferences impossible to satisfy, producing [[Frustrated Ising Constraint System|frustration]]. That conflict is the optimization signal: the ground state violates as few edge preferences as possible.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

