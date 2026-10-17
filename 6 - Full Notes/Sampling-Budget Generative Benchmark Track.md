2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Sampling-Budget Generative Benchmark Track

Track T1 fixes the total number of queries drawn from each trained generative model and permits the cost function to be evaluated for all of them. It represents settings in which sampling is scarce or expensive but candidate scoring is comparatively cheap.

The paper uses $Q=10^4$ queries to compute quality coverage, minimum value, and utility. This track is particularly relevant to a QCBM executed on quantum hardware because repeated circuit measurements can dominate evaluation cost, even when the classical objective is inexpensive.

A fixed query count tests how efficiently probability mass is allocated to valuable solutions. It does not account for samples consumed during training in this experiment, so the reported race compares post-training sampling effectiveness rather than total end-to-end resource use.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

