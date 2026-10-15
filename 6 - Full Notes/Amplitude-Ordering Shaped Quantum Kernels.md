2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Amplitude-Ordering Shaped Quantum Kernels

When image pixels are stored as quantum amplitudes, qubit adjacency does not automatically equal image adjacency. A two-qubit gate mixes groups of four amplitudes, and the amplitude indices in each group depend on which adjacent qubit pair the gate acts upon. Reordering pixels before state preparation therefore determines the spatial pattern represented by that gate's effective kernel.

Row-major ordering makes one gate mix horizontal groups while another reaches regularly spaced pixels. Alternative orderings can group square neighborhoods or combine vertical and horizontal lines. More generally, a gate on $K$ adjacent qubits mixes groups of $2^K$ amplitudes. This gives amplitude loading a second architectural role beyond compression: the index map defines the receptive fields available to later local gates. Random ordering tends to break those spatial relationships and reduced accuracy in the paper's fully quantum experiments.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
