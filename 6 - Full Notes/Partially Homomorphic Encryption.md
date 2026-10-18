2026-10-18 16:30

Status: #baby

Tags: [[Privacy-Preserving Encryption]]

# Partially Homomorphic Encryption

Partially homomorphic encryption supports one homomorphic operation—such as addition or multiplication—an unlimited number of times. It does not support unrestricted composition of both operations, so the computations expressible under encryption remain limited to the scheme's preserved algebraic structure.

The source lists unpadded RSA and ElGamal among constructions with multiplicative homomorphism and Goldwasser-Micali as another example. This capability can be useful, but the same structure may also permit controlled changes to ciphertext and create malleability concerns unless the broader protocol supplies integrity protection. It is the narrowest category within [[Homomorphic Encryption]].

# References

[[cryptographyandcryptanalysisinjava.epub]]
