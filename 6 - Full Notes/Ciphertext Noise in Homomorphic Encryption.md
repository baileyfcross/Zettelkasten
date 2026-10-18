2026-10-18 16:30

Status: #baby

Tags: [[Privacy-Preserving Encryption]]

# Ciphertext Noise in Homomorphic Encryption

Ciphertext noise is auxiliary variation carried by a homomorphic ciphertext and enlarged by encrypted operations. The noise helps support the scheme's security, but correct decryption requires it to remain below a bound. Repeated evaluations eventually raise it until the ciphertext can no longer be decoded reliably.

Noise growth explains the depth limit in [[Somewhat Homomorphic Encryption]]. [[Fully Homomorphic Encryption]] overcomes that limit through a refresh operation rather than by pretending evaluation is free. Parameter choices must therefore balance security, the intended computation, ciphertext size, and the remaining noise budget.

# References

[[cryptographyandcryptanalysisinjava.epub]]
