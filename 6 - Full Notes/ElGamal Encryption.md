2026-10-18 16:30

Status: #baby

Tags: [[Public-Key Cryptosystems and Digital Identity]]

# ElGamal Encryption

ElGamal encryption is a public-key scheme defined over a cyclic group. A private exponent (x) produces a public group element (h=g^x). For each message, the sender chooses a fresh random value (y), publishes (g^y) as one ciphertext component, and combines the message with the shared group value (h^y) as the other. The recipient reconstructs the same shared value with the private exponent and removes it.

The construction relies on discrete-logarithm and Diffie-Hellman assumptions. Its multiplicative structure also makes basic ElGamal malleable, so encryption must be combined with authentication or a protocol designed to resist chosen-ciphertext attacks.

# References

[[cryptographyandcryptanalysisinjava.epub]]
