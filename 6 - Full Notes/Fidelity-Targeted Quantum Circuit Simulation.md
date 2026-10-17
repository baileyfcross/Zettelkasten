2026-10-17 17:30

Status: #baby

Tags: [[Quantum Algorithm Execution and Verification]]

# Fidelity-Targeted Quantum Circuit Simulation

A classical circuit simulator can trade computational cost against a specified fidelity target instead of insisting on exact evolution. Tensor-network cuts, truncation, or partial path evaluation can approximate the output closely enough for a benchmark or hardware-verification goal.

The target must be stated because an approximate simulation and an exact amplitude calculation support different claims. A simulator tuned only to reproduce a verification statistic may be much cheaper than one that reconstructs the full ideal distribution, which is why classical comparison should match the experimental accuracy requirement.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

