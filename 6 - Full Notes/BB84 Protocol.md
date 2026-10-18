2026-10-18 16:30

Status: #baby

Tags: [[Quantum and Post-Quantum Cryptography]]

# BB84 Protocol

BB84 is a [[Quantum Key Distribution]] protocol that encodes random bits in one of two bases, commonly described through rectilinear and diagonal photon polarizations. The sender chooses a bit and basis independently for every state; the receiver independently chooses a measurement basis. A matching basis recovers the intended bit, while an incompatible basis gives an unreliable result.

After transmission, the parties compare basis choices over a classical channel without revealing the bit values and retain only matching positions. They then test for errors and apply correction and privacy amplification. The source's Java example simulates bit and basis bookkeeping only; a genuine implementation requires quantum states, a quantum channel, sources, and detectors.

# References

[[cryptographyandcryptanalysisinjava.epub]]
