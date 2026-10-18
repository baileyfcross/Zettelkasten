2026-10-18 16:30

Status: #baby

Tags: [[Symmetric Encryption Algorithms and Modes]]

# Galois Counter Mode

Galois Counter Mode is a mode of operation that extends counter-based encryption with an authentication result. The counter portion produces encrypted counter blocks that are combined with plaintext, while the completed operation returns both ciphertext and an authentication tag.

That pairing addresses two distinct needs: encryption conceals the content and the authentication value lets a recipient detect unauthorized modification. GCM is therefore more than a way to divide data into blocks. It is a composition that provides confidentiality and integrity together when used with an appropriate [[Encryption Key]] and correctly handled initialization data.

# References

[[cryptographyandcryptanalysisinjava.epub]]
