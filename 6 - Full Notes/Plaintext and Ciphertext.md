2026-09-14 02:44

Status: #baby

Tags: [[Symmetric Encryption Algorithms and Modes]]

# Plaintext and Ciphertext

Plaintext is the original readable input to an encryption process, while ciphertext is the scrambled output intended to conceal that meaning. Plaintext may represent text, images, audio, video, or other digital data rather than only written words.

[[Encryption]] combines plaintext with an [[Encryption Key]] to produce ciphertext, and decryption combines ciphertext with the appropriate key to recover plaintext. Security depends on the transformation and key, not on ciphertext merely looking unfamiliar.

Block ciphers operate on fixed-size representations of plaintext, so longer messages must be divided into blocks and processed through a [[Block Cipher Mode of Operation]]. Text encodings, padding, and Base64 transport are separate representation steps: Base64 can make ciphertext printable, but it does not add cryptographic protection.

# References

[[cybersecurity.epub]]

[[cryptographyandcryptanalysisinjava.epub]]
