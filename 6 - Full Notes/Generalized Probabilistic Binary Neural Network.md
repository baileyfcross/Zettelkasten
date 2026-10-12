2026-10-12 02:19

Status: #baby

Tags: [[Quantum-Deformed Probabilistic Neural Networks]]

# Generalized Probabilistic Binary Neural Network

A generalized probabilistic binary neural network inserts a learned stochastic transformation between a layer's input distributions and its deterministic binary layer map. The transformation jointly maps incoming activations and sampled weights to new activation-weight pairs, so it can represent dependencies that a fully factorized probabilistic binary network excludes.

The layer then averages its ordinary binary computation over this correlated joint distribution. Setting the transformation's deformation parameters to zero recovers the standard factorized model, making the generalized network a strict extension rather than a separate prediction formalism.

In the quantum construction, the stochastic transformation is induced by measurement probabilities after an entangling unitary. [[Quantum-Deformed Layer Correlation Operator]] therefore connects this classical probabilistic definition to the paper's quantum circuit.

# References

[[2020 - Quantum Deformed Neural Networks.pdf]]
