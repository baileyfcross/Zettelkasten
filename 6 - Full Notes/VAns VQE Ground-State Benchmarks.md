2026-10-12 17:40

Status: #baby

Tags: [[Variable-Structure Variational Quantum Circuits]]

# VAns VQE Ground-State Benchmarks

The paper tests VAns as a variational quantum eigensolver on four- and eight-qubit transverse-field Ising and XXZ Heisenberg chains, plus four-qubit H2 and eight-qubit linear H4 molecular Hamiltonians. The spin-model simulations use several coupling or anisotropy values, while the molecular calculations use STO-3g orbitals and a Jordan-Wigner mapping.

For the Ising model, reported relative energy errors stay below 6 x 10^-5 at four qubits and 8 x 10^-4 at eight qubits. The four-qubit XXZ errors stay below 9 x 10^-7, while eight-qubit errors are around 10^-3 and rise in a region where local optimization can settle on low-lying excited states. H2 and H4 results fall within the paper's chemical-accuracy threshold across the tested bond lengths.

These are small, classically simulated experiments; the noiseless cases are reported from one run per problem. Their strongest structural observation is that insertion initially grows the Ising circuit, after which simplification can reduce CNOTs and trainable parameters while further lowering the energy relative to the selected hardware-efficient baselines.

# References

[[2022 - A semi-agnostic ansatz with variable structure for quantum machine learning.pdf]]
