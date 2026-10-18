2026-10-18 16:30

Status: #baby

Tags: [[Privacy-Preserving Encryption]]

# Homomorphic Evaluation

Homomorphic evaluation applies a supported function to encrypted inputs and produces another ciphertext. The operation uses a public evaluation key, so a computing service can perform the transformation without holding the private key required to reveal either the inputs or the result.

Correctness connects the encrypted and plaintext domains: decrypting the evaluated ciphertext must return the same value as applying the corresponding plaintext function to the original messages. The range of permitted functions and the number of safe compositions determine whether the surrounding [[Homomorphic Encryption]] scheme is partial, somewhat homomorphic, or fully homomorphic.

# References

[[cryptographyandcryptanalysisinjava.epub]]
