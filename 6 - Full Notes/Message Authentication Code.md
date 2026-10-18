2026-09-14 02:44

Status: #baby

Tags: [[Cryptographic Randomness and Hashing]]

# Message Authentication Code

A message authentication code is a short keyed value that lets a recipient check both message integrity and possession of the shared authentication key. Altering the message or lacking the key prevents an attacker from producing the expected code.

Unlike an unkeyed [[Cryptographic Hash Function|hash]], the code authenticates a party that holds the key. The source presents it as a lighter form of signature evidence used to support [[Nonrepudiation]].

Java's cryptographic architecture exposes MAC algorithms as services alongside hashes, ciphers, and signatures. The shared secret distinguishes a MAC from an ordinary digest: both can detect changed content, but only the keyed construction limits valid code generation to parties that possess the authentication key.

# References

[[cybersecurity.epub]]

[[cryptographyandcryptanalysisinjava.epub]]
