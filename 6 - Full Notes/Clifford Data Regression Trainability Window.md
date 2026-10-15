2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Clifford Data Regression Trainability Window

Clifford data regression learns an affine map from paired noisy and classically simulated expectation values of training circuits chosen to be predominantly Clifford. The fitted map is then used to correct nearby target-circuit cost evaluations.

When the same map is applied locally across parameter space, [[Linear Error-Mitigation Ansatz Resolvability Invariance]] shows that the method need not worsen concentration-driven resolution. This creates a practical window in which it can repair [[Noise-Driven Cost Landscape Corruption]] and improve optimization before the circuit enters the exponentially concentrated NIBP regime.

The advantage is conditional. The affine parameters can depend on the circuit, training data must be generated and measured, and a map learned in one region may not transfer across the full landscape. The paper's theoretical resolvability calculation also omits this training-data burden.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
