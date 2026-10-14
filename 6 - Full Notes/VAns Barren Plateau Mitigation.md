2026-10-12 17:40

Status: #baby

Tags: [[Variable-Structure Variational Quantum Circuits]]

# VAns Barren Plateau Mitigation

VAns is intended to mitigate two depth-related sources of flat optimization landscapes. Random circuits approaching a unitary 2-design generally need substantial depth and parameter count, so pruning both makes it less likely that the ansatz becomes excessively expressive. Noise-induced barren plateaus instead worsen directly with circuit depth, making shallow layouts valuable even when randomness is not the cause.

This is a design argument rather than a general proof that VAns avoids barren plateaus. The paper suggests strengthening it by monitoring reduced-state second Rényi entropy with classical shadows and preferring architecture steps that hold entanglement constant or reduce it.

Empirical support comes from [[VAns Noise-Adaptive Circuit Depth]], where the search responds to stronger simulated noise by retaining fewer gates. The benchmark shows useful depth adaptation in the tested model, while the paper leaves broader investigation of noise-induced barren-plateau mitigation to future work.

# References

[[2022 - A semi-agnostic ansatz with variable structure for quantum machine learning.pdf]]
