2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# Bloch-Sphere Label States for Quantum Classification

A label-state classifier assigns each class a target pure state $|\phi_c\rangle$ on the Bloch sphere. Training moves the output for each example toward the state representing its class, and inference chooses the label with the largest output-state fidelity.

The target states should be placed as far apart as possible to maximize distinguishability. Two classes can occupy antipodal states, while three or more classes must share the sphere with smaller pairwise separations because a single qubit has only two orthogonal states.

This geometry lets one qubit represent multiclass decisions without adding readout qubits, but closely packed labels can reduce the margin between competing fidelities. [[Single-Qubit Readout Quantum Classifier]] describes how the experiment measures each overlap directly, and [[Fidelity-Loss Quantum Classification]] describes how those targets define training.

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
