2026-10-12 18:17

Status: #baby

Tags: [[Policy-Gradient Variational Quantum Compilation]]

# Policy-Gradient Quantum Compilation Benchmark

The paper compares endpoint-reward policy gradient with COBYLA and Powell optimization on random target circuits of 10, 15, and 20 qubits with respective depths 3, 4, and 5. The main distance experiment averages sequences of 200, 100, and 50 runs as the initialization moves farther from the known optimum.

Policy gradient usually retains higher endpoint fidelity, and its advantage becomes more pronounced at larger qubit counts near the onset of the barren plateau. Cross-sections show cost fluctuations of roughly one percent at ten qubits but below 10^-4 at twenty qubits, where the two gradient-free methods have much less signal to exploit.

Resource comparison is not exact: each policy update evaluates several episodes, learning rate affects convergence, and episode sampling is parallelizable. The study uses Cirq simulation, selected shallow random circuits, and only two gradient-free baselines; it does not report quantum-hardware execution or establish superiority over every gradient-based or reinforcement-learning alternative.

# References

[[2022 - Policy Gradient Approach to Compilation of Variational Quantum Circuits.pdf]]
