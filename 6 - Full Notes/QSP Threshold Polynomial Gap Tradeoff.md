2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# QSP Threshold Polynomial Gap Tradeoff

A bounded polynomial cannot reproduce a discontinuous VaR step uniformly at its jump. The QSP construction therefore leaves a transition gap of width $\Delta$ around the threshold and limits the approximation error to $\epsilon$ on the intervals outside that gap. Narrowing $\Delta$ makes the threshold sharper but requires a higher degree, with analytic constructions scaling as $O(\!\left(\Delta^{-1}\log(1/\epsilon)\right))$.

The paper obtains near-optimal even polynomials by expanding in [[Chebyshev Polynomial|even Chebyshev polynomials]] and solving a minimax problem on Chebyshev-root grid points while enforcing a magnitude bound slightly below one. For the VaR probability, the resulting threshold error scales approximately as $O(1/d)$ with degree $d$. Polynomial error and the outer amplitude-estimation error must be balanced, because improving one below the resolution of the other no longer improves the final estimate.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
