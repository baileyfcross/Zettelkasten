2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Quantum Data Learning for High-Energy Physics

Quantum data learning trains or evaluates a model directly on quantum states rather than first converting every measurement into a classical feature vector. In high-energy physics, an immediate use is to extract phase or dynamical information from states produced by a digital or analog quantum simulation, including transitions such as confinement and deconfinement that may not have a simple local order parameter.

Learning only selected observables can require far fewer state copies than reconstructing the complete density matrix. Full tomography of an unknown $n$-qubit state has exponential sample complexity, while restricted learning tasks such as predicting a fixed family of observables or learning structured state classes can scale polynomially. The scientific question should therefore determine what information is measured instead of defaulting to full reconstruction.

A longer-term proposal connects quantum sensors coherently to a quantum processor so information can be processed before classical measurement destroys its quantum character. That route faces demanding requirements in transduction, coherence, noise mitigation, and measurement overhead. It differs fundamentally from applying a quantum classifier to ordinary collider tables: the possible advantage comes from retaining quantum input structure, not only from using a quantum circuit as a model.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
