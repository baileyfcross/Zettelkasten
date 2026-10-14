2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Connectivity-Aware Quantum Classifier Architecture Benchmark

A circuit architecture's nominal two-qubit gate count can hide routing overhead. The Fashion-MNIST simulations compare one- and two-dimensional sequential circuits, MERA, and QCNN classifiers while counting every logical two-qubit gate as three CNOTs under ideal connectivity.

The one-dimensional nearest-neighbor circuit slightly outperforms the alternatives at comparable nominal CNOT counts and maps directly to many devices. The two-dimensional grid and hierarchical MERA/QCNN layouts require connections absent from ibmq-kolkata's heavy-hex topology, so SWAP insertion would make their physical counts larger than the plotted values. Architecture comparisons should therefore distinguish logical expressivity from compiled resource cost on the target processor.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
