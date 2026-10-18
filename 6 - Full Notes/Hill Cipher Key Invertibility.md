2026-10-18 16:30

Status: #baby

Tags: [[Classical Ciphers and Cryptanalysis]]

# Hill Cipher Key Invertibility

A Hill cipher key must be a square matrix that has an inverse modulo the alphabet size. For the 26-symbol construction in the source, this requires the matrix determinant to be coprime with 26. Without that condition, no modular inverse exists and distinct plaintext blocks can collapse into outputs that cannot be uniquely reversed.

This requirement connects key generation to correct decryption: selecting an arbitrary matrix is not sufficient. The [[Hill Cipher]] must validate the matrix before it is used, because the same modular structure that performs encryption determines whether recovery is mathematically possible.

# References

[[cryptographyandcryptanalysisinjava.epub]]
