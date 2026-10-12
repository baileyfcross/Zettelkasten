2026-10-12 17:40

Status: #baby

Tags: [[Variable-Structure Variational Quantum Circuits]]

# VAns Quantum Autoencoder Benchmark

The paper trains a [[Quantum Autoencoder]] with VAns to compress four-qubit H2 ground states into a two-qubit subsystem. Six molecular states at different bond lengths form the training set and ten additional states form the test set; fixed VAns-generated circuits prepare those states before a second VAns search learns the encoder.

Training minimizes a local cost that measures each trash qubit separately, avoiding the global projector cost associated with barren plateaus at larger sizes. In one reported run, the cost reaches approximately 10^-7 within 15 accepted architecture modifications. The learned circuit uses about 45 parameters, compared with 180 in the 15-layer hardware-efficient baseline, while obtaining a cost about two orders of magnitude lower.

The reported mean values of -log10(1-F) are 6.49 on training states and 6.17 on test states, where F is encoding-decoding fidelity. Because this is one simulated instance on a small molecular dataset, it supports resource-efficient architecture search for this task rather than a broad generalization claim.

# References

[[2022 - A semi-agnostic ansatz with variable structure for quantum machine learning.pdf]]
