2026-10-12 01:33

Status: #baby

Tags: [[Enhanced Feature Quantum Autoencoders]]

# EF-QAE Ising Ground-State Compression

The paper evaluates enhanced feature quantum autoencoding on six-qubit ground states of a one-dimensional transverse-field Ising model. Twenty evenly spaced ground states with transverse fields from 0.5 through 1.0 form the training set, and the field value itself serves as the model feature.

The circuit uses three layers and discards two trash qubits, leaving a four-qubit compressed state. Training averages the [[Local Trash-Qubit Compression Cost]] over the twenty states and uses BFGS for classical optimization. Compared with the same-depth standard QAE, the feature-conditioned model reaches a lower cost but requires more function evaluations.

Tests at field values 0.60 and 0.75 show that the enhanced model concentrates more trash-state weight at the all-zero state and produces higher reconstruction fidelity. Across twenty training and sixty test states, it usually has higher fidelity, with several exceptions near a field of 0.7 that the paper suggests addressing through denser or nonuniform training samples.

# References

[[2021 - Quantum autoencoders with enhanced data encoding.pdf]]
