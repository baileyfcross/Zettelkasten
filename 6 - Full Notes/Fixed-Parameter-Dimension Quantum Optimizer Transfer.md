2026-10-17 11:48

Status: #baby

Tags: [[Meta-Learned Variational Quantum Optimization]]

# Fixed-Parameter-Dimension Quantum Optimizer Transfer

A recurrent optimizer with fixed input and output widths can transfer across quantum system sizes when the ansatz has the same number of variational parameters at every size. QAOA-like circuits satisfy this condition when parameter count depends on depth $P$ rather than on the number of qubits.

The study exploits that invariance by training on small, classically simulatable circuits and testing on larger circuits from the same problem class. The quantum state space grows, but the optimizer still receives and emits vectors of the dimensions it saw during training.

This is system-size transfer, not arbitrary model-size transfer. An ansatz whose parameter count expands with qubit count would require an architecture able to process variable-length parameter sets or a different optimizer for each size.

# References

[[2019 - Learning to learn with quantum neural networks via classical neural networks.pdf]]

