2026-10-12 17:40

Status: #baby

Tags: [[Variable-Structure Variational Quantum Circuits]]

# VAns Identity-Compiling Gate Dictionary

The VAns gate dictionary contains parameterized gate sequences that equal the identity at designated parameter values. In the paper's main simulations, these sequences are built from rotations about the x and z axes and CNOT gates, including blocks that add a general single-qubit unitary or entangle a selected pair of qubits.

Identity compilation makes a newly expanded circuit initially equivalent to its predecessor: inserting the block does not immediately change the cost, but later parameter optimization can move through the enlarged circuit family. The paper notes that small deviations from exact identity may be allowed to expand the available dictionary.

The dictionary is a point of task and hardware customization. It can use native gates to avoid compilation overhead or restrict blocks to preserve a problem symmetry, which is why the broader [[Variable Ansatz Algorithm]] is described as semi-agnostic rather than completely problem-independent.

# References

[[2022 - A semi-agnostic ansatz with variable structure for quantum machine learning.pdf]]
