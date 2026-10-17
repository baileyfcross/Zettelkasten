2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Probability Integral Transform for Quantum Generation

The probability integral transform maps each continuous variable $X_i$ through its marginal cumulative distribution $F_i$, producing $U_i=F_i(X_i)$ with a uniform marginal on $[0,1]$. Applied coordinate by coordinate, it removes the original marginal shapes while preserving the joint dependence in a copula.

In data-driven use, the cumulative marginals are approximated from empirical histograms and inverted after generation. The transformed model can focus on dependencies among uniform variables rather than simultaneously learning marginal distributions and correlations.

The transform alone does not guarantee easier learning. It improves the benchmark most when paired with [[Quantum Copula Generator Architecture]], whose circuit enforces uniform marginals structurally. The same PIT data offer inconsistent benefits to the generic continuous circuit because that ansatz must still learn the marginal constraint.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

