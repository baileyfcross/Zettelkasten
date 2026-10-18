2026-10-18 16:30

Status: #baby

Tags: [[Classical Ciphers and Cryptanalysis]]

# Known-Plaintext Attack on Hill Cipher

A known-plaintext attack on the [[Hill Cipher]] uses one or more plaintext blocks together with their matching ciphertext blocks to recover the key matrix. Encryption is a linear matrix transformation modulo 26, so enough aligned input-output vectors can be arranged into equations and inverted to solve for that transformation.

The attack illustrates why an elegant mathematical operation does not automatically provide secrecy. When an adversary knows samples on both sides of a linear mapping, the samples disclose structure that ciphertext-only obscurity would otherwise hide. The book also notes that common digraph frequencies can help attack a two-by-two construction.

# References

[[cryptographyandcryptanalysisinjava.epub]]
