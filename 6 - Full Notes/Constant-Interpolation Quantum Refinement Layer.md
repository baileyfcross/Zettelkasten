2026-10-12 19:52

Status: #baby

Tags: [[Hierarchical Multigrid Variational Quantum Algorithms]]

# Constant-Interpolation Quantum Refinement Layer

A constant-interpolation quantum refinement layer extends an n-qubit variational circuit by appending a new qubit in the plus state and coupling it to every existing qubit. For each old qubit, the layer applies a controlled-Z gate, a parameterized Y rotation on the new qubit, and a second controlled-Z gate.

Every new rotation parameter is initialized to zero. The two controlled-Z gates around an identity rotation then cancel, so the inherited state becomes the equal superposition of attaching zero and one to each computational-basis component. This preserves the coarse solution as a constant interpolation at the start of the refined optimization.

Later optimization can move the new rotations away from zero and entangle the added degree of freedom with the existing register. The design assumes all-to-all coupling between the new qubit and older qubits; reducing its entangling gates for restricted hardware connectivity is left as future work. [[Coarse-to-Fine Variational Parameter Transfer]] carries the old angles into this layer.

# References

[[2023 - Hierarchical Multigrid Ansatz for Variational Quantum Algorithms.pdf]]
