2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Generator Ansatz

The A-qGAN generator initializes every qubit with a Hadamard gate and then repeats layers of parameterized $R_Y$ rotations followed by controlled-$Z$ entanglers. With $n$ qubits and $k_G$ repeated layers, the construction contains $(k_G+1)n$ trainable rotations and $k_Gn$ controlled-$Z$ gates.

This ansatz keeps the parameter count linear in feature dimension while allowing amplitudes to become correlated across qubits. The real-valued $R_Y$ rotations align naturally with the angle-encoded input range, and the controlled-$Z$ pattern supplies entanglement without introducing additional trainable two-qubit parameters.

Depth controls both capacity and trainability. Too few layers may not represent the background distribution, while excessive depth increases noise exposure and the risk of vanishing gradients. In the benchmark, the three-feature model uses three generator repetitions and six trainable parameters, whereas the seven-feature model uses nine repetitions and seventy parameters. [[qGAN Effective Dimension Capacity]] evaluates how much model space these constrained generators cover.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
