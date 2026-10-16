2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# Nested Monte Carlo Complexity for Derivative Risk

Classical derivative-risk analysis nests an inner Monte Carlo price inside an outer sampling of market scenarios. If price error is $\epsilon_p$ and scenario-sampling error is $\epsilon_S$, the cost scales as $O(\epsilon_S^{-2}\epsilon_p^{-2})$. Assigning both errors the same order as a target $\epsilon$ gives $O(\epsilon^{-4})$.

A semi-classical method replaces only the inner pricing calculation with quantum amplitude estimation, improving the scaling to $O(\epsilon_S^{-2}\epsilon_p^{-1})$ or $O(\epsilon^{-3})$. Fully coherent QAE and QSP risk algorithms can reach approximately $\widetilde O(\epsilon^{-2})$ when their scenario state is still built from classical samples. If a full scenario distribution can instead be loaded efficiently, its discretization error may fall exponentially with qubit count, but [[Quantum Scenario Preparation Bottleneck|state preparation]] then becomes part of the claimed advantage.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
