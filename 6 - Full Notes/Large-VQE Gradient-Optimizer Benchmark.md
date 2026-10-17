2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Large-VQE Gradient-Optimizer Benchmark

The largest experiments optimized random ten-term VQE Hamiltonians on 20 qubits with 160 parameters and 25 qubits with 200 parameters. Computational cost forced these simulations to omit shot noise and use adjoint differentiation, so only gradient-based optimizers were compared.

Adam achieved the best observed loss on both large tasks and therefore a normalized difference of zero. AMSGrad followed at $0.1748$, NAdam at $0.2234$, RMSProp at $0.3080$, and Adamax at $0.3211$; the remaining gradient methods were much farther behind.

These two cases show that the adaptive-gradient ordering persisted at larger simulated parameter counts. They do not test measurement-limited scaling, derivative-free competition, chemically realistic Hamiltonians, or noisy hardware, and therefore cannot establish a large-device optimizer ranking.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

