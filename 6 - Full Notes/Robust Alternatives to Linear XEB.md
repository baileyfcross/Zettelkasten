2026-10-17 03:33

Status: #baby

Tags: [[Random-Circuit Quantum Advantage Verification]]

# Robust Alternatives to Linear XEB

Replacing linear XEB with a logarithmic or otherwise nonlinear score can remove its approximately additive growth across disconnected subsystems. That change alone does not prevent deviations from fidelity or the amplification of a weak correlation by classical post-processing. A repaired score must be evaluated against all three vulnerabilities rather than only its system-size scaling.

Total variation distance is insensitive to the simple top-$k$ amplification logic, but estimating it for an exponentially large output domain requires impractically many samples in the regimes of interest. Fidelity can bound it usefully only when fidelity is already very high. Faster-scrambling gates, deeper circuits, and nonlocal connectivity can raise the cost of partition attacks, while interactive cryptographic protocols can shift verification away from a single distribution score. The paper therefore treats robust, experimentally efficient quantum-advantage verification as an open design problem.

# References

[[2024 - Limitations of Linear Cross-Entropy as a Measure for Quantum Advantage.pdf]]

