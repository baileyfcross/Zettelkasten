2026-10-12 17:40

Status: #baby

Tags: [[Variable-Structure Variational Quantum Circuits]]

# Variable Ansatz Algorithm

The Variable Ansatz algorithm, or VAns, constructs a parameterized quantum circuit while the variational optimization is running. Instead of fixing the gate layout in advance, it alternates between growing the circuit with identity-compiling blocks, simplifying the resulting layout, and retraining the surviving continuous parameters.

Its inputs include a task cost function, an initial circuit, a dictionary of parameterized gates, insertion and simplification rules, optimizers for continuous and discrete choices, and a termination condition. The method is semi-agnostic because the search procedure is reusable, while the gate dictionary, initial circuit, cost, and stopping rule can still encode hardware or problem knowledge.

VAns is designed to find enough expressibility for a task without allowing circuit depth and parameter count to grow unchecked. [[VAns Stochastic Identity Block Insertion]] supplies new capacity, [[VAns Informed Circuit Simplification]] removes redundancy, and the [[VAns Discrete-Continuous Optimization Loop]] decides whether a new architecture is retained.

# References

[[2022 - A semi-agnostic ansatz with variable structure for quantum machine learning.pdf]]
