2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Quantum Derivative Pricing Pipeline

Derivative pricing estimates the discounted expectation of a contract's payoff over possible future paths of its underlying assets. A quantum pricing circuit separates this into probability loading, payoff encoding, and expectation estimation.

A preparation operator $P$ creates $\sum_\omega\sqrt{p(\omega)}|\omega\rangle$. A payoff operator $F$ then makes a designated ancilla's good-state probability equal to the normalized payoff $f(\omega)$ for each path. The composite operator $A=FP$ therefore produces a total good-state probability $\sum_\omega p(\omega)f(\omega)=\mathbb{E}[f]$.

Quantum amplitude estimation estimates that probability, providing the proposed quadratic sampling improvement over classical [[Monte Carlo Integration]]. The main engineering question is how to implement $P$ and $F$ cheaply enough for this asymptotic advantage to survive; [[Quantum Arithmetic Bottleneck in Derivative Pricing]] identifies the payoff-side obstacle targeted by QSP.

For portfolio risk, the path and payoff construction can be conditioned on an outer market-scenario register. The resulting [[Scenario-Conditioned Quantum Portfolio Pricing Oracle]] sums contract payoffs for each path and exposes the normalized portfolio value $V(s)$ while retaining the scenario label, allowing VaR and CVaR algorithms to reuse the pricing pipeline coherently across possible future markets.

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
