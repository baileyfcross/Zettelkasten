2026-10-18 16:30

Status: #baby

Tags: [[Classical Ciphers and Cryptanalysis]]

# Hill Cipher

The Hill cipher is a polygraphic substitution cipher that encrypts blocks of letters together. Letters are converted to numbers, arranged as a vector, multiplied by a square key matrix, and reduced modulo the alphabet size. The numeric result is then converted back into ciphertext letters.

Block size follows the matrix dimension, so a final short block must be padded. Decryption uses the inverse of the key matrix modulo 26, which means [[Hill Cipher Key Invertibility]] is a requirement rather than merely an implementation convenience. Its linear form also enables a [[Known-Plaintext Attack on Hill Cipher]].

# References

[[cryptographyandcryptanalysisinjava.epub]]
