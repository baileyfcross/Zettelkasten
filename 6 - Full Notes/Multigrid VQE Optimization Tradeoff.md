2026-10-12 19:52

Status: #baby

Tags: [[Hierarchical Multigrid Variational Quantum Algorithms]]

# Multigrid VQE Optimization Tradeoff

Multigrid VQE trades additional classical optimization work for a more informative starting point at each larger problem size. Rather than asking one fixed circuit to solve the final instance from an unrelated initialization, it repeatedly optimizes a coarse level, refines the circuit, preserves old angles, and optimizes the new level.

Across the paper's Dirichlet Laplacian, MaxCut, and Maximum Exact k-SAT simulations, this process produces better average objective values than a static Efficient SU(2) ansatz but generally makes more function evaluations. The benchmark plots also show less variation in the multigrid optimizer-call count. Better solution quality therefore does not imply lower classical cost.

A Laplacian comparison combines COBYLA at the coarse stages with BFGS after refinement and contrasts it with BFGS on the same multigrid-shaped circuits initialized entirely at zero. The transferred runs remain better as size increases, supporting [[Coarse-to-Fine Variational Parameter Transfer]] rather than circuit shape alone. The evidence comes from finite noiseless simulations and does not establish convergence or runtime scaling on hardware.

# References

[[2023 - Hierarchical Multigrid Ansatz for Variational Quantum Algorithms.pdf]]
