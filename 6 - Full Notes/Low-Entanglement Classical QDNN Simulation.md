2026-10-12 02:19

Status: #baby

Tags: [[Quantum-Deformed Probabilistic Neural Networks]]

# Low-Entanglement Classical QDNN Simulation

The classically simulated quantum-deformed layer restricts its deformation to a shallow one-dimensional circuit of alternating nearest-neighbor two-qubit gates. Activation and weight qubits are interleaved, and the gates couple either an activation with its weight or a weight with the next activation.

This local structure keeps the observables needed for an output neuron's mean and variance confined to small neighborhoods: the paper's circuits act on four sites for the mean and six for the relevant variance term. Their expectation values can consequently be evaluated in linear time in the number of inputs and parallelized across local regions.

Classical tractability is purchased by excluding the highly entangling circuits that motivate [[Quantum-Deformed Sampling Speedup]]. The simulation also clones the input activation distribution for separate output neurons—an exact classical operation but only an approximate quantum one—and factors the output channels before applying the [[Weak-Correlation Gaussian QDNN Approximation]].

# References

[[2020 - Quantum Deformed Neural Networks.pdf]]
