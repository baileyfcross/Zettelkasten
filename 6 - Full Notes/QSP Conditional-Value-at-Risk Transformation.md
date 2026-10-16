2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# QSP Conditional-Value-at-Risk Transformation

After the VaR threshold is known, QSP can estimate the conditional tail value by applying a function that retains the encoded value below the threshold and maps larger values to zero. Because the input singular value is a square root of the normalized scenario price, the marked-state probability becomes the probability-weighted sum $\sum_{V(s)\leq V_\alpha}p(s)V(s)$.

Dividing that amplitude-estimated quantity by the tail probability gives $C_\alpha$, and subtracting it from today's value gives [[Conditional Value at Risk for Derivative Portfolios|CVaR]]. A direct retained-value function is discontinuous at the threshold and therefore expensive to approximate accurately. [[Inverted CVaR Threshold Function]] reformulates the same tail expectation with a continuous-at-threshold target requiring a lower polynomial degree.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
