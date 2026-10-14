2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Trainable Bitstring Observable Readout

A trainable bitstring observable readout converts the probability vector from measuring $m$ qubits into $k$ class scores with an affine map $\widetilde s=As+b$. Equivalently, each class observable is a trainable diagonal linear combination of computational-basis projectors, so all $k$ observables commute and can be evaluated from the same set of shots.

Training $A$, $b$, and the quantum circuit together removes the requirement that one measured bit string correspond directly to one class. In the Fashion-MNIST simulations, this readout lets a circuit use roughly one fewer quantum layer for similar accuracy and match the unprocessed four-qubit readout while measuring only three qubits. The additional classical capacity motivates the [[Classical Readout Contribution Audit]].

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
