2026-10-18 16:30

Status: #baby

Tags: [[Quantum and Post-Quantum Cryptography]]

# Hybrid NTRU and AES Encryption

Hybrid NTRU and AES encryption uses the [[NTRU Cryptosystem]] for compact key material and the [[Advanced Encryption Standard]] for the message body. The source's Java workflow generates an AES key and initialization vector, encrypts the plaintext with AES, concatenates the key and IV, and encrypts that smaller block with the NTRU public key.

The recipient separates the NTRU block from the AES ciphertext, decrypts the first block with the NTRU key pair, recovers the AES key and IV, and then decrypts the message. This is a post-quantum instance of [[Hybrid Public-Key Encryption]] and keeps the expensive public-key operation away from the bulk payload.

# References

[[cryptographyandcryptanalysisinjava.epub]]
