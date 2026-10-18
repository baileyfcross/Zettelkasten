2026-10-18 16:30

Status: #baby

Tags: [[Public-Key Cryptosystems and Digital Identity]]

# Merkle-Hellman Knapsack Cryptosystem

The Merkle-Hellman cryptosystem encodes a message's bits as a subset-sum problem. Its private sequence is superincreasing: every element is larger than the sum of all preceding elements, which makes the private subset sum recoverable greedily. Modular multiplication disguises that sequence to form the public weights, and encryption sums the public weights selected by the message bits.

Decryption uses the private modular inverse to return to the easy superincreasing problem. The original scheme was proved insecure, but it remains instructive because it demonstrates the trapdoor goal of [[Asymmetric Encryption]]: publish an apparently difficult problem while retaining private structure that makes reversal efficient.

# References

[[cryptographyandcryptanalysisinjava.epub]]
