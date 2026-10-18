2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]] [[Symmetric Encryption Algorithms and Modes]]

# Initialization Vector

An initialization vector supplies varying input to a block-cipher mode so identical plaintext encrypted with the same key does not begin with identical ciphertext. It influences the first block and, through the mode, the blocks that follow.

An IV normally does not need to be secret, but its uniqueness or unpredictability requirements must be respected for the chosen mode. It is commonly stored alongside the ciphertext while the encryption key is protected separately.

In the Java AES example, CBC mode receives the same IV for encryption and the matching decryption operation. The source warns that its hard-coded demonstration value is educational only and recommends generating the IV randomly in practice. The example also keeps the IV separate from the password-derived [[Encryption Key]] and its [[Cryptographic Salt]].

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[cryptographyandcryptanalysisinjava.epub]]
