2026-10-17 03:33

Status: #baby

Tags: [[Random-Circuit Quantum Advantage Verification]]

# Top-k XEB Amplification

When a classical algorithm can calculate its entire approximate output distribution $q$, it can rank bitstrings by $q(x)$ and sample only from the $k$ highest-probability strings. If $q$ is positively correlated with the ideal distribution $p$, this top-$k$ selection increases the average ideal probability of the reported samples and therefore amplifies XEB.

The method optimizes the reported distribution for the benchmark after simulation rather than improving its fidelity to the target circuit. Very small $k$ can overfit circuit-to-circuit fluctuations, so the mean correlation must remain positive and the variance must be controlled. [[Self-Averaging XEB Spoofing]] supplies that control and yields a standard deviation that decreases approximately as $1/\sqrt{k}$.

# References

[[2024 - Limitations of Linear Cross-Entropy as a Measure for Quantum Advantage.pdf]]

