2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Natural-Gradient Learning-Rate Stability

Multiplying a coordinate gradient by the inverse Fubini-Study metric changes both its direction and its effective scale. In the optical experiments, this preconditioning permits a larger nominal learning rate on the rugged Hex-GKP task while retaining a smoother loss curve than vanilla gradient descent or Adam.

The paper interprets the smooth trajectory as evidence that the inverted metric makes the parameter landscape seen by the optimizer better conditioned. The claim is local and empirical: the metric does not literally alter the loss function, but it changes how a step in parameter coordinates maps to a change of quantum state.

A larger stable learning rate contributes to convergence in fewer update steps. It does not by itself establish lower total computational cost, because each natural-gradient step must also construct and invert a metric approximation.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

