2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Correction-Unitary QCBM Depth Growth

Training a deeper QCBM from scratch becomes harder as the number of free parameters grows. The benchmark instead trains one repeated circuit block, preserves its fitted parameters, appends a new block initialized to the identity, and then optimizes the enlarged model.

The added block begins as a correction unitary: it leaves the shallower solution unchanged at initialization and can learn only the residual transformation needed to improve it. This warm start mitigates convergence failures compared with simultaneously randomizing all parameters at every depth.

This procedure changes the optimization path as well as circuit capacity, so performance at greater depth is conditional on the earlier fitted solution. The QGAN experiments are cold-started because their selected architectures did not require this intervention.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

