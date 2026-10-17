2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# Noise-Model Drift in Error Mitigation

Noise-aware mitigation inverts a learned hardware model, so temporal changes between characterization and circuit execution create a common systematic error for PEC, ZNE, and TEM. Superconducting-qubit environments can drift because of microscopic fluctuators, control imprecision, and non-Markovian effects, making periodic relearning necessary.

If the relative per-layer error fluctuations have standard deviation $\Theta$, independent layer-to-layer deviations partly cancel and give a typical relative bias of approximately $\tfrac12\epsilon N\sqrt{L}\Theta$. The square-root dependence on depth reflects stochastic drift rather than a coherent worst-case accumulation. For the paper's $100\times100$ example with $\epsilon=0.16\%$ and $\Theta=1.8\%$, this contribution is about 1.44 percent.

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

