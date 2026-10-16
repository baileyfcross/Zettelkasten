2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# Value at Risk for Derivative Portfolios

Value at risk, or VaR, measures a portfolio's depreciation at a chosen confidence level over a specified horizon. A derivative portfolio is repriced under possible future market scenarios, producing values $V(s)$ with probabilities $p(s)$. The lower-tail value $V_\alpha$ is the smallest value whose cumulative probability reaches $1-\alpha$, and the reported risk is

$$
\operatorname{VaR}_\alpha[V]=V_0-V_\alpha,
$$

where $V_0$ is today's portfolio value.

For a finite equally weighted scenario set, the classical calculation sorts the scenario prices and selects the $1-\alpha$ percentile. The metric identifies a quantile, not the size of losses deeper in the tail; [[Conditional Value at Risk for Derivative Portfolios]] supplies that complementary expectation. Quantum methods replace repeated scenario-by-scenario pricing with a [[Quantum Market Scenario Superposition]] and a coherent estimate of the same lower-tail probability.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
