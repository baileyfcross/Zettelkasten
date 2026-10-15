2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Fidelity Concentration Limitation

The residual term in the [[A-qGAN Composite Anomaly Score]] compares an event state with the learned generator state through global fidelity. Although fidelity gives a direct similarity measure, overlaps between high-dimensional quantum states can concentrate into a narrow range as qubit count grows. Distinguishing ordinary from anomalous inputs may then require increasingly precise expectation estimates.

This concentration is related to trainability problems in quantum kernels: a formally valid distance measure can lose practical resolution even before circuit noise is considered. More measurement shots do not change the underlying separation; they only estimate an already concentrated value more accurately, potentially at exponential sampling cost.

The small three-to-eight-feature experiments do not establish that fidelity remains useful at collider scale. A scalable A-qGAN therefore needs a distance measure whose contrast survives increasing dimension, perhaps by using structured or local observables rather than a single global overlap. The paper leaves that choice as an open research problem rather than treating the demonstrated fidelity score as a finished large-scale solution.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
