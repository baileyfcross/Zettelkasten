2026-09-06 21:16

Status: #baby

Tags: [[Spatial Tracking and Registration]] [[Bayesian Information Fusion]]

# Sensor Fusion

Sensor fusion combines measurements from multiple sensors to obtain tracking behavior that no single input provides reliably. Complementary sensors measure different degrees of freedom, competitive sensors provide redundant estimates, and cooperative sensors derive information from their combined observations.

The measurements may differ in coordinate system, rate, latency, accuracy, and noise. Fusion therefore requires calibration and temporal alignment as well as a rule or statistical filter for reconciling the evidence.

A Bayesian fusion model treats the quantity being estimated as a hidden variable and conditions each sensor likelihood on it. Conditional independence offers a simple product of evidence, while explicit dependency, ancillary clues, and false-alarm variables prevent repeated or unreliable measurements from being counted as independent support.

# References

[[augmentedreality_pearson.pdf]]

[[bayesianprogramming.pdf]]
