2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# QAE Digitization Leakage in Value-at-Risk Estimation

An $m$-qubit coherent amplitude estimate represents a scenario price as a distribution over nearby binary values rather than as one exact value. A comparator can therefore allocate some amplitude to the wrong side of a VaR threshold: a true value below $\mu$ may contribute to the above-threshold flag, and a value above $\mu$ may contribute below it.

Increasing $m$ concentrates the estimate around the true price and reduces this leakage, but the cost grows because the controlled QAE powers require $2^m+1$ calls to the pricing oracle and its inverse. The inner estimator in [[Coherent QAE Value-at-Risk Estimation]] must also remain coherent, so measurement-based iterative QAE variants cannot simply replace it even when they would be efficient for a final scalar readout. [[QSP versus QAE Value-at-Risk Resources]] avoids the digital register by transforming the price amplitude directly.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
