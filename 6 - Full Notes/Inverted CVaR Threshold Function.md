2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# Inverted CVaR Threshold Function

The inverted CVaR threshold function replaces a retained-value target that jumps to zero at the VaR cutoff with

$$
\widehat\theta_\mu(x)=\begin{cases}\mu-x,&x\leq\mu,\\0,&x>\mu.\end{cases}
$$

Both branches meet at zero, so a bounded polynomial can approximate the target with substantially lower degree than a discontinuous linear threshold.

Applied at the VaR cutoff, amplitude estimation returns the expected gap between the threshold and values in the lower tail. If that conditional gap is $\widehat C_\alpha=\mu_\alpha-C_\alpha$, then the original conditional tail value is recovered as $C_\alpha=\mu_\alpha-\widehat C_\alpha$. The reformulation changes the encoded quantity, not the definition of [[Conditional Value at Risk for Derivative Portfolios|CVaR]].

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
