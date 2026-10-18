2026-10-18 16:30

Status: #baby

Tags: [[Classical Ciphers and Cryptanalysis]]

# Vigenere Cipher

The Vigenere cipher is a polyalphabetic substitution cipher. A keyword is repeated until it matches the message length, and each key letter selects the shift applied to the plaintext letter at the same position. The same plaintext symbol can therefore map to different ciphertext symbols as the key position changes.

This variation hides single-letter frequencies better than the [[Caesar Cipher]], but a recurring keyword also introduces a period. Once an analyst estimates that period with a method such as the [[Kasiski Examination]], the ciphertext can be divided into positions governed by the same shift and treated as several Caesar ciphers.

# References

[[cryptographyandcryptanalysisinjava.epub]]
