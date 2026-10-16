2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# Scenario-Conditioned Quantum Portfolio Pricing Oracle

A scenario-conditioned quantum pricing oracle preserves a market-scenario label while encoding the normalized portfolio value as an ancilla probability:

$$
A|s\rangle|0\rangle|0\rangle=|s\rangle\left(\sqrt{V(s)}|\psi_0^s\rangle|0\rangle+\sqrt{1-V(s)}|\psi_1^s\rangle|1\rangle\right).
$$

It extends the [[Quantum Derivative Pricing Pipeline]] by making the market data controlled by the scenario register. For a portfolio, the path generator covers all relevant market factors and the payoff operation sums the normalized discounted payoffs of the constituent contracts before encoding their expectation.

When preceded by [[Quantum Market Scenario Superposition]], one invocation exposes $V(s)$ for every scenario coherently. [[Coherent QAE Value-at-Risk Estimation]] digitizes those amplitudes, while [[QSP Threshold Transformation for Value at Risk]] acts on them directly as block-encoded singular values.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
