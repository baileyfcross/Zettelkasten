2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Inference Algorithms]]

# Variable Elimination

Variable elimination answers a probabilistic query by summing or integrating free variables out of factored distributions in a chosen order. It reuses intermediate results instead of expanding the entire joint distribution.

Elimination order strongly affects the size of those intermediate factors. Conditional independence makes the approach efficient when it prevents many variables from becoming coupled during computation.

# References

[[bayesianprogramming.pdf]]
