2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]]

# Initialization Vector

An initialization vector supplies varying input to a block-cipher mode so identical plaintext encrypted with the same key does not begin with identical ciphertext. It influences the first block and, through the mode, the blocks that follow.

An IV normally does not need to be secret, but its uniqueness or unpredictability requirements must be respected for the chosen mode. It is commonly stored alongside the ciphertext while the encryption key is protected separately.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
