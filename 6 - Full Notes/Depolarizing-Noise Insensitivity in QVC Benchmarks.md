2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Depolarizing-Noise Insensitivity in QVC Benchmarks

Adding a depolarizing channel with probability $p=0.01$ after every gate produced little separation between optimizer performance in the review. A follow-up VQE plot for Adam, AMSGrad, and NAdam remained noisy and oscillatory but showed no clear degradation trend for tested values below $p=0.05$.

This result is evidence about one simulated channel, not general noise robustness. Real devices combine coherent errors, drift, readout error, crosstalk, nonuniform gate noise, and finite calibration, none of which is captured by a homogeneous depolarizing channel.

The apparent insensitivity should therefore be treated as a limitation of the benchmark's noise probe as much as a property of the optimizers. The authors explicitly call for hardware experiments and richer noise studies before drawing practical conclusions.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

