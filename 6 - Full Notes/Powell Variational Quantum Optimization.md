2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Powell Variational Quantum Optimization

Powell's direction-set method was one of the strongest non-parameter-shift choices in the variational-circuit review. It performs bidirectional line searches along a collection of search directions, avoiding explicit componentwise quantum gradients while still organizing a multidimensional local search.

When every learning-rate configuration was kept separate, Powell had the best average rank, $7.1379$. Its average normalized loss difference was $1.4188$, substantially worse than the strongest Adam variants, so its good relative placement did not translate into the best absolute loss quality.

The method is therefore a credible black-box baseline, not a resource-free alternative. Its line searches can require many objective evaluations, and the study did not normalize those evaluations against the shifted circuits used by gradient methods.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

