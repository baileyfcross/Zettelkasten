2026-10-17 17:30

Status: #baby

Tags: [[Quantum Algorithm Execution and Verification]]

# Tensor-Network Quantum Circuit Simulation

Tensor-network simulation represents a quantum circuit as a network of multidimensional arrays and chooses a contraction order that sums internal indices without materializing the full $2^n$ state vector. Strategic cuts divide a difficult network into subproblems whose memory and parallelism can be managed on classical HPC systems.

The NASA work cited in the lecture used memory tradeoffs and large distributed runs to compute selected amplitudes for random circuits beyond ordinary state-vector capacity. Cost still depends strongly on circuit connectivity, depth, contraction width, and the number of amplitudes requested, so qubit count alone does not predict simulation difficulty.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

