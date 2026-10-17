2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Quantum-Classical Learned Optimization Loop

A variational quantum algorithm can be viewed as a temporal computational graph. At step $t$, a classical controller proposes circuit parameters $\theta_t$, the quantum processor prepares the corresponding state and estimates a cost $y_t$, and the estimate returns to the controller to determine the next parameters.

Unrolling this loop exposes every proposal, circuit evaluation, measurement, and state update as part of one sequence. That representation makes it possible to replace a hand-designed classical update rule with an optimizer that is itself learned across many related cost functions.

The same graph has two operating modes. Meta-training differentiates through the unrolled sequence to improve the classical controller, while deployment can treat the quantum circuit as a black box and require only measured function values.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

