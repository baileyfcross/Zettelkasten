2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# SWAP-Test State-Fidelity Invertibility Loss

The state-fidelity invertibility loss compares the forward circuit's premeasurement state with the state reconstructed from its measured output by inverse state preparation. A SWAP test estimates their overlap, and training pushes that fidelity toward one.

Matching the states is sufficient for invertibility because applying the inverse unitary will then recover the original encoded input. It is not necessary, however: exponentially many reconstructed states can produce the same recovered input after the inverse circuit and final measurement.

This makes fidelity a stricter objective than the classical map actually requires. In the collider experiment it also creates substantial artifacts in the lepton-separation distribution when combined with the MMD term, motivating the more flexible [[Reconstruction MSE Invertibility Loss]].

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

