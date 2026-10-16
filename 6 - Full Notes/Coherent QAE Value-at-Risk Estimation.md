2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# Coherent QAE Value-at-Risk Estimation

Coherent QAE value-at-risk estimation uses two amplitude-estimation layers. An inner coherent QAE circuit converts each scenario-conditioned price amplitude from the [[Scenario-Conditioned Quantum Portfolio Pricing Oracle]] into an $m$-qubit value register without measuring the scenario superposition. A comparator marks whether the represented value lies below a VaR candidate $\mu$, and an outer QAE invocation estimates the total marked probability $P[V\leq\mu]$.

Repeating the construction inside a [[Bisection Method|bisection search]] finds the smallest candidate whose cumulative probability reaches $1-\alpha$. Canonical QAE naturally digitizes the angle $\arcsin\sqrt{V(s)}$ rather than $V(s)$, but comparing that angle with $\arcsin\sqrt\mu$ preserves the ordering and avoids an extra arithmetic conversion. Finite inner precision creates the [[QAE Digitization Leakage in Value-at-Risk Estimation|digitization-leakage error]].

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
