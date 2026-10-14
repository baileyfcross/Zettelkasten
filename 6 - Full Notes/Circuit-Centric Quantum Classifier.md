2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Circuit-Centric Quantum Classifier

A circuit-centric quantum classifier is a hybrid supervised-learning model whose trainable core is a low-depth parameterized quantum circuit. It separates inference into four stages: encode a classical feature vector as a quantum state, transform it with a model circuit, estimate a measurement probability, and classically threshold that probability after adding a learned bias.

One design uses [[Amplitude Encoding for Circuit-Centric Classification]], so an $N$-dimensional input can occupy approximately $\lceil\log_2 N\rceil$ qubits. Its model circuit is assembled from parameterized one-qubit gates and controlled one-qubit gates organized as [[Strongly Entangling Quantum Classifier Block|strongly entangling blocks]]. A [[Single-Qubit Readout Quantum Classifier|single-qubit readout]] supplies the continuous score.

An alternative [[Single-Qubit Data Re-Uploading Classifier]] eliminates a separate amplitude-state loader. It inserts classical features directly into rotation angles at every layer, uses circuit depth as model capacity, and compares the output qubit with class-specific label states. This preserves the circuit-centric pattern while exchanging qubit width for repeated, accurately controlled operations.

A second structured alternative uses [[Unary Amplitude Encoding]] and [[Reconfigurable Beam Splitter Quantum Gate|reconfigurable beam-splitter gates]]. In a [[Quantum-Assisted Neural Network]], the circuit estimates inner products inside an otherwise classical network. In a [[Quantum Orthogonal Neural Network]], a [[Quantum Pyramidal Circuit]] realizes an exactly orthogonal weight matrix on the unary subspace. These designs sacrifice the logarithmic qubit width of general amplitude encoding to gain a transparent correspondence with classical neural-network layers.

Training remains hybrid: a quantum processor estimates outputs and analytical derivatives, while a classical optimizer stores and updates parameters. The resulting parameter count can grow polynomially in the qubit count and therefore polylogarithmically in the input dimension, although [[Circuit-Centric Quantum Classifier Resource Scaling]] shows that general state preparation can erase this advantage.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
