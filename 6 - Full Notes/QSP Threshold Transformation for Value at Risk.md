2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# QSP Threshold Transformation for Value at Risk

The derivative-pricing oracle block-encodes the scenario value through the singular value $\sqrt{V(s)}$. A QSP VaR circuit chooses a bounded polynomial that approximates the threshold function

$$
\theta_\mu(x)=\begin{cases}1,&x\leq\mu,\\0,&x>\mu,\end{cases}
$$

and applies it coherently to every scenario amplitude. The marked-state probability then approximates $P[V(s)\leq\mu^2]$ without first constructing a binary price register.

An outer amplitude-estimation routine reads that probability, and [[Adaptive QAE Bisection for Value at Risk]] varies $\mu$ until it reaches the target lower-tail mass $1-\alpha$. The approximation is not an exact comparator: [[QSP Threshold Polynomial Gap Tradeoff]] determines how the transition region and polynomial degree contribute error.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
