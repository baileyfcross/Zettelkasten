2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# Structured Ansatz Sensitivity to Coherent Leakage

A structured variational ansatz explores a physically motivated subset of Hilbert space rather than an unrestricted state family. This economy can reduce the number of optimization parameters, but it also makes systematic coherent errors especially harmful: repeated miscalibrated gates can push the prepared state outside the manifold that gives the ansatz its physical meaning.

The paper studies this effect with UCC-SD circuits for molecular VQE. These circuits can contain roughly $10^3$ noisy two-qubit gates, so coherent errors near $10^{-3}$ per entangling gate can accumulate into a large energy error even while decoherence is neglected. [[Coherent CNOT Error Models for VQE]] make this sensitivity explicit, and [[Coherent-Error Response Linearization]] explains why noise tailoring helps.

The conclusion is specific to deep, structured circuits under systematic gate errors. It does not imply that every expressive restriction is fragile or that coherent leakage is the only limitation of UCC-SD.

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
