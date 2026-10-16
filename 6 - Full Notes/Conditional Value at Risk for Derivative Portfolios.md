2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# Conditional Value at Risk for Derivative Portfolios

Conditional value at risk, or CVaR, measures the expected depreciation when the portfolio is already in the tail beyond its [[Value at Risk for Derivative Portfolios|VaR threshold]]. If $V_\alpha$ is the lower-tail portfolio value, the conditional tail value is

$$
C_\alpha=\frac{1}{1-\alpha}\sum_{V(s)\leq V_\alpha}p(s)V(s),
$$

and $\operatorname{CVaR}_\alpha[V]=V_0-C_\alpha$.

VaR answers where the tail begins, whereas CVaR summarizes the severity of values inside that tail. The quantum construction first finds the VaR threshold and then uses a [[QSP Conditional-Value-at-Risk Transformation]] to encode the probability-weighted tail value. It therefore inherits uncertainty from both the threshold estimate and the subsequent amplitude estimate.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
