2026-09-06 21:47

Status: #baby

Tags: [[Probability Foundations]]

# Conditional Independence

Variables $X$ and $Y$ are conditionally independent given $Z$ when knowing $Y$ adds no information about $X$ once $Z$ is known: $P(X \mid Y,Z)=P(X \mid Z)$.

This is weaker and more useful than unconditional independence. Bayesian decomposition uses conditional independence to replace a large joint distribution with smaller factors, reducing inference and learning cost while retaining dependencies explained through the conditioning variables.

# References

[[bayesianprogramming.pdf]]
