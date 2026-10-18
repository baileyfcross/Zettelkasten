2026-10-18 16:30

Status: #baby

Tags: [[Java Platform Cryptography and Security]]

# JCA Engine Class

A JCA engine class exposes one category of cryptographic service through a consistent Java API. The application calls a factory such as `getInstance` with an algorithm name, and the [[Java Cryptography Architecture]] locates an implementation through an installed [[Cryptographic Service Provider]].

Different engines represent different jobs: `Cipher` transforms data, `MessageDigest` computes a hash, `Signature` signs or verifies, `KeyPairGenerator` creates related public and private keys, `KeyGenerator` creates shared secret keys, `KeyAgreement` establishes a shared key, and `SecureRandom` supplies security-sensitive random values. The abstraction separates service use from provider implementation.

# References

[[cryptographyandcryptanalysisinjava.epub]]
