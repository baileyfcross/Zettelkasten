2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# QN-SPSA Pauli Two-Design Benchmark

The paper tests QN-SPSA on layered Pauli two-design circuits with nearest-neighbor controlled-$Z$ gates and random single-qubit rotation axes. An 11-qubit, three-layer instance has 44 parameters, while a 22-qubit, five-layer instance has 132 parameters.

On the smaller problem, QN-SPSA approaches the convergence of an exact quantum natural gradient and outperforms ordinary SPSA and vanilla gradient descent, though its trajectories have greater stochastic variance. The exact method also exhibits occasional spikes when its Fubini-Study matrix is unstable to invert.

For 22 qubits the analytic natural-gradient baseline is omitted because its estimated circuit demand is about 2.6 million, compared with 2,100 evaluations for the QN-SPSA run. This demonstrates the intended query-scaling contrast, but only on a local diagonal observable and simulated shot noise rather than a broad class of hardware workloads.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

