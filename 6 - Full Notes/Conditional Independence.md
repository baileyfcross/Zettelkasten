2026-09-06 21:47

Status: #baby

Tags: [[Probability Foundations]] · [[High-Dimensional Graphical Models]]

# Conditional Independence

Variables $X$ and $Y$ are conditionally independent given $Z$ when knowing $Y$ adds no information about $X$ once $Z$ is known: $P(X \mid Y,Z)=P(X \mid Z)$.

This is weaker and more useful than unconditional independence. Bayesian decomposition uses conditional independence to replace a large joint distribution with smaller factors, reducing inference and learning cost while retaining dependencies explained through the conditioning variables.

Graphical models use conditional rather than marginal dependence to represent direct relationships. Two variables may be strongly correlated because of a shared cause yet become independent once that cause is conditioned on. In a [[Gaussian Graphical Model]], the relevant conditional independences are encoded by zeros of the precision matrix.

# References

[[bayesianprogramming.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
