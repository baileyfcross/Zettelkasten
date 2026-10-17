2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Quantum Generator Qubit-Shot Tradeoff

Continuous and discrete quantum generators allocate scarce hardware resources differently. A continuous generator uses one qubit per feature but requires many circuit shots to estimate the expectation vector for every generated sample. A discrete generator uses $r$ qubits per feature but obtains a complete grid sample from one shot.

The better choice depends on whether qubits or repeated execution time is the dominant constraint. Near-term devices may favor the small continuous register, while high-throughput sampling can favor the wider discrete circuit once sufficient qubits and resolution are available.

This tradeoff is obscured by state-vector simulation. Exact expectation values make the continuous circuit unusually cheap, while simulating the wider discrete state and sampling from it is relatively expensive. [[Simulator-Hardware Architecture Reversal]] explains why simulator wall time should not be treated as hardware performance.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

