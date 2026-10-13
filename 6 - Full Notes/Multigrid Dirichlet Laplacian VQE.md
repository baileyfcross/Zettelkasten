2026-10-12 19:52

Status: #baby

Tags: [[Hierarchical Multigrid Variational Quantum Algorithms]]

# Multigrid Dirichlet Laplacian VQE

Multigrid Dirichlet Laplacian VQE prepares an approximate ground state of the one-dimensional finite-difference Dirichlet operator by increasing the encoded resolution one qubit at a time. The smallest eigenvectors form progressively smoother, roughly parabolic amplitude profiles, giving adjacent levels the refinement structure needed by [[Coarse-to-Fine Variational Parameter Transfer]].

The paper simulates two through twelve qubits, corresponding at the largest level to 4,096 state-vector amplitudes. Compared with a separately optimized Efficient SU(2) circuit at each size, the multigrid circuit continues reducing its estimated eigenvalue after the static baseline has largely flattened. With 1,000 shots it eventually reports error near 0.01, and with one million shots error near 0.001, while using more optimizer evaluations.

The experiment uses Qiskit's noiseless Aer simulator and an Efficient SU(2) seed chosen as a proof of concept rather than by a multigrid theorem. The rapidly shrinking true ground energy also increases the shots needed to maintain absolute accuracy. These conditions limit the result to evidence that the hierarchy is useful in this benchmark, not a hardware or asymptotic advantage.

# References

[[2023 - Hierarchical Multigrid Ansatz for Variational Quantum Algorithms.pdf]]
