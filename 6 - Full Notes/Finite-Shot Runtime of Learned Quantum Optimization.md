2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Finite-Shot Runtime of Learned Quantum Optimization

An objective query is not one quantum-circuit execution. Estimating a Hamiltonian expectation to a target precision requires repeated measurements, with a bound that scales as $O(\lVert H\rVert_*^2/\epsilon^2)$ for Pauli-decomposed costs.

For the test distributions and cost-noise variance $0.05$, the paper estimates roughly $(7\pm4)\times10^5$ repetitions per MaxCut query, $(2.3\pm0.6)\times10^4$ per spin-glass query, and $(3\pm2)\times10^5$ per Hubbard query. At 10,000 repetitions per second, the ten LSTM steps take about $700\pm400$, $23\pm6$, and $300\pm200$ seconds respectively.

These estimates show why reducing query count matters while also preventing ten queries from being confused with ten shots. They are workload-level projections based on ideal circuit execution plus sampling, not measured wall-clock runtimes on a noisy processor.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

