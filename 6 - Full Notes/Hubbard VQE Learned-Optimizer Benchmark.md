2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Hubbard VQE Learned-Optimizer Benchmark

The Hubbard-model benchmark uses a five-step Trotter-inspired VQE ansatz. Each step has separate parameters for horizontal hopping, vertical hopping, and on-site interaction, so the recurrent optimizer handles fifteen parameters at every lattice size.

Training contains 10,000 half-filled instances split between $2\times2$ and $3\times2$ lattices, with hopping $t=1$ and interaction strength $U$ sampled uniformly from $0.1$ to $4.0$. Testing moves to a $4\times2$ lattice while preserving the same ansatz dimension and uses a fermionic swap network for the circuit structure.

The LSTM again finds a useful point in ten queries, but noisy Nelder-Mead refinement is much less effective here than in the two QAOA tasks. The benchmark therefore supports transferable initialization while also showing that local fine-tuning quality depends on the application landscape.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

