2026-10-18 16:30

Status: #baby

Tags: [[Quantum and Post-Quantum Cryptography]]

# Quantum Key Distribution Eavesdropping Detection

Quantum key distribution detects eavesdropping by testing for disturbances introduced when an interceptor measures transmitted quantum states without knowing the correct preparation basis. A wrong-basis measurement changes the state available to the intended receiver and raises the observed error rate.

The legitimate parties reveal and compare only a sample of their sifted key. If the error rate is unacceptable, they reject the exchange rather than trusting the candidate secret. If it is acceptable, they continue with error correction and [[Quantum Key Distribution Privacy Amplification]]. Detection is therefore statistical evidence from the protocol, not a claim that every individual interception announces itself directly.

# References

[[cryptographyandcryptanalysisinjava.epub]]
