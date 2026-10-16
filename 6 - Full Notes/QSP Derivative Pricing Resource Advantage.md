2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# QSP Derivative Pricing Resource Advantage

For an autocallable benchmark with three assets, 20 timesteps, and payoff-amplitude error at most $10^{-3}$, square-root-driven QSP reduces the amplitude-estimation operator from 36,000 to 7,800 T-depth, from 6.6 million to 414,000 T gates, and from 19,200 to 4,700 logical qubits. These correspond to improvements of about 4.7, 16, and 4.1 times over the selected lookup-table-plus-arithmetic baseline.

Extending the calculation through iterative amplitude estimation at total error $10^{-3}$ and confidence $0.68$ gives an estimated 4,700 logical qubits, T-depth $4.5\times10^7$, and T-count $2.4\times10^9$. Matching an assumed one-second classical price requires a 45 MHz logical T-gate rate, compared with 207 MHz for the arithmetic method.

These are fault-tolerant resource estimates under a specific stochastic model, contract, error allocation, classical baseline, and circuit decomposition. They quantify a lower threshold, not a demonstrated quantum advantage or an assessment of present hardware readiness.

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
