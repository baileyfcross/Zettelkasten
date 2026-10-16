2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# QLSTM Variational Subnetwork Ansatz

Each quantum neural subnetwork in the finance QLSTM uses four qubits and one ansatz layer. Its data-loading stage applies Hadamard gates, then encodes each scalar input $x_i$ with $R_y(\arctan x_i)$ and $R_z(\arctan x_i^2)$ rotations.

The variational stage entangles the register with cyclic CNOT patterns in which every qubit acts as a control for neighbors at offsets one and two. A measurement layer converts the quantum state back into classical values used by the surrounding [[Quantum-Enhanced LSTM Cell Architecture]]. The output $y_t$ is represented with a three-qubit one-hot encoding for the sentiment classes.

The reported circuit is a selected experimental architecture rather than a uniquely required QLSTM design. [[QLSTM Sentiment Training Behavior]] shows that even this shallow choice becomes expensive under classical circuit simulation, while adding layers is associated with a longer training delay.

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
