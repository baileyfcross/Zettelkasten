2026-10-18 16:30

Status: #baby

Tags: [[Quantum and Post-Quantum Cryptography]]

# Quantum Key Distribution

Quantum key distribution creates shared key material by encoding random candidate bits into quantum states and sending them through a quantum channel. The receiver measures each state using independently selected bases. The parties then use a classical channel to reveal and compare only their basis choices, discarding positions measured with incompatible bases.

The remaining positions form a sifted key rather than an immediately trusted final key. The parties disclose a sample to estimate the error rate, use that evidence for [[Quantum Key Distribution Eavesdropping Detection]], correct acceptable errors, and apply [[Quantum Key Distribution Privacy Amplification]] before retaining the secret. [[BB84 Protocol]] is the book's primary example.

# References

[[cryptographyandcryptanalysisinjava.epub]]
