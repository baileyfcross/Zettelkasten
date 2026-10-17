2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# Error-Mitigation Resource Forecasting

A scalable mitigation forecast combines random and systematic errors rather than quoting sampling overhead alone. The shot budget follows from wall time and per-execution latency, while systematic terms account for [[Noise-Model Drift in Error Mitigation]], ZNE extrapolation bias, and TEM compression or measurement approximations.

For PEC and ZNE, classical post-processing is comparatively small, but the quantum-shot overhead differs sharply. TEM uses the optimal shot exponent while adding a classical contraction whose cost grows approximately cubically with bond dimension. Under the paper's assumed timing, error stability, and classical resources, lowering the per-layer error toward $0.16\%$ opens a predicted region near dense $100\times100$ circuits where TEM can keep total observable error below roughly ten percent within practical wall time. This is a forecast under a modeled noise regime, not an experimental advantage demonstration.

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

