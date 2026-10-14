2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Sparse Staircase Quantum Image Encoding Ansatz

The sparse staircase ansatz repeats nearest-neighbor blocks containing two arbitrary one-qubit rotations and one CNOT. It replaces a general $SU(4)$ two-qubit block, whose compilation on ibmq-kolkata requires three CNOTs and about 25 native single-qubit gates, with a block already close to the device's native operations.

One sparse layer has about one-third the compiled depth and two-fifths the parameters of one general layer. On the 11-qubit Fashion-MNIST encoding task, three sparse layers reach 95.1% mean state fidelity, about one percentage point below two general layers while using half as many CNOTs and roughly one-third the depth. The design trades a small loss in approximation for greater hardware fidelity.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
