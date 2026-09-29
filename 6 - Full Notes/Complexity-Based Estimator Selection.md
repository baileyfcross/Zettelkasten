2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Model Selection]]

# Complexity-Based Estimator Selection

Complexity-based estimator selection compares a manageable collection of fitted estimators through a criterion that includes fit, approximation to candidate model spaces, and a complexity penalty. It adapts model-selection theory to choose among tuning parameters or estimation methods without repeatedly splitting the data.

Using the full sample can be valuable when $n$ is small, and the Gaussian version described in the source has nonasymptotic risk guarantees. The tradeoff is narrower applicability: those guarantees depend on the noise model and on constructing an appropriate model family. It complements, rather than universally replaces, [[Cross-Validation]].

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
