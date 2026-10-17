2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# High Learning Rates in QVC Optimization

Learning rates of $0.01$ and especially $0.1$ consistently outperformed $0.001$ and $0.0001$ for the parameter-shift optimizers in the reviewed variational circuits. The authors report that the smaller rates remained inferior even when allowed enough iterations to converge under the experiment's stopping rules.

This differs from common defaults in classical neural-network training. The benchmark establishes the empirical pattern but does not explain it theoretically, leaving open whether periodic circuit geometry, gradient scale, shot noise, ansatz structure, or the finite iteration budget produces the preference.

A high learning rate should consequently be a search candidate rather than a universal prescription. Replication across hardware, circuit families, parameterizations, and objectives is needed before transferring the value outside the tested suite.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

