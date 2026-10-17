2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Normalizing-Flow Change-of-Variables Objective

A normalizing flow learns a bijection $f$ that maps data $x$ to a simple latent variable $z=f(x)$, commonly with a standard Gaussian distribution. Generation reverses the map by sampling $z$ and evaluating $f^{-1}(z)$.

The likelihood follows from [[Change of Variables in Multiple Integrals]]:

$$p(x\mid\theta)=p_Z(f(x\mid\theta))\left|\det J_f(x)\right|.$$

For a Gaussian latent distribution, the negative log-likelihood combines a squared latent norm with $-\log|\det J_f|$, plus an optional parameter prior. A model can therefore serve as an exact density estimator when its transformation is invertible and its [[Jacobian Determinant]] is tractable. Classical coupling flows enforce those properties architecturally; a [[Quantum Invertible Neural Network]] instead uses unitary structure plus auxiliary losses to repair the noninvertible measurement step.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

