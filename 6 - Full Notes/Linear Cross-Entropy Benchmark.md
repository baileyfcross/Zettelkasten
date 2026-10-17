2026-10-17 03:33

Status: #baby

Tags: [[Random-Circuit Quantum Advantage Verification]]

# Linear Cross-Entropy Benchmark

The linear cross-entropy benchmark (XEB) measures correlation between an observed bitstring distribution $q$ and an ideal random-circuit distribution $p$. For an $N$-qubit circuit, the population value is $\chi_p(q)=2^N\sum_x p(x)q(x)-1$. Samples that are uncorrelated with the ideal probabilities give an average near zero, while samples from a sufficiently chaotic ideal circuit give an average near one.

XEB is experimentally attractive because it can be estimated by evaluating the ideal probability of each sampled bitstring; its sampling error falls roughly as the inverse square root of the number of samples. That convenience does not make it a universal distance between distributions. [[Benign and Adversarial Quantum Benchmarking]] separates its use as a device diagnostic from its much stronger use as evidence against every classical competitor.

# References

[[2024 - Limitations of Linear Cross-Entropy as a Measure for Quantum Advantage.pdf]]

