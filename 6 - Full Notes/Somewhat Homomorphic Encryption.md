2026-10-18 16:30

Status: #baby

Tags: [[Privacy-Preserving Encryption]]

# Somewhat Homomorphic Encryption

Somewhat homomorphic encryption supports both addition and multiplication on ciphertext, but only for a limited evaluation depth. Each operation consumes part of the scheme's remaining capacity, so a computation that composes too many operations can make the result undecryptable.

This category is more expressive than [[Partially Homomorphic Encryption]] because both fundamental operations are available, yet it stops short of arbitrary circuits. The limiting mechanism is commonly [[Ciphertext Noise in Homomorphic Encryption|ciphertext noise]], whose growth must stay inside the scheme's decryption bound.

# References

[[cryptographyandcryptanalysisinjava.epub]]
