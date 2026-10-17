2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# QCBM Line-Topology Generative Benchmark

A quantum circuit Born machine prepares $U(\theta)|0\rangle^{\otimes N}$ and measures every qubit in the computational basis. Born probabilities from the parameterized wavefunction define a generative distribution over bitstrings without a separate decoder.

The benchmark uses 20 qubits, eight variational layers, nearest-neighbor connectivity on a line, and 256 trainable parameters. Parameters begin uniformly between $-\pi/2$ and $\pi/2$ and are optimized without gradients by CMA-ES with initial scale $\sigma_0=0.1$ to minimize regularized forward KL divergence from the reweighted training distribution.

An all-to-all circuit performs worse at this scale because of trainability, despite having worked at 12 qubits in earlier experiments. The probabilities are calculated exactly in simulation; a larger or hardware implementation would need sample-based losses and would expose finite-shot and device-noise costs absent from the reported comparison.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

