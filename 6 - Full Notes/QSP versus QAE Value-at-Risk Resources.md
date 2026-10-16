2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# QSP versus QAE Value-at-Risk Resources

The coherent-QAE VaR method performs an analog-to-digital-to-analog path: it digitizes each price amplitude, compares the binary value with a threshold, and re-encodes the result as a marked probability. With $m$ value qubits, that stage uses $2^m+1$ pricing-oracle calls and introduces [[QAE Digitization Leakage in Value-at-Risk Estimation|digitization leakage]].

The QSP method directly approximates a threshold on the price amplitude. A degree-$d$ polynomial uses $d-1$ pricing-oracle calls, one additional signal qubit, and controlled phase rotations instead of the QAE value register and its reflections. In simulations with 5,000 normally distributed scenario prices and 100 repetitions per point, QSP required about ten times fewer oracle calls than coherent QAE for the same VaR error. Both methods had similar asymptotic scaling; the reported advantage is a finite-resource comparison for the tested regime.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
