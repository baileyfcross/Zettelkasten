2026-09-14 02:44

Status: #baby

Tags: [[Symmetric Encryption Algorithms and Modes]]

# Encryption Key

An encryption key is a value supplied to a cryptographic algorithm to control how data is transformed. The source describes keys as unpredictable bit strings whose length and protection affect the difficulty of recovering protected information.

A strong algorithm cannot preserve confidentiality after its necessary secret keys are stolen. [[Symmetric Encryption]] shares one secret, while [[Asymmetric Encryption]] divides public and private roles between a related key pair.

The source distinguishes key generation from the cipher operation that consumes the key. DES derives round-specific subkeys from one shared secret, AES accepts defined secret-key sizes, and public-key schemes generate a related pair. In each case, unpredictability, valid parameter selection, storage, and distribution are part of the key's security rather than properties supplied by ciphertext alone.

# References

[[cybersecurity.epub]]

[[cryptographyandcryptanalysisinjava.epub]]
