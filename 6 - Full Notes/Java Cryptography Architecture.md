2026-10-18 16:30

Status: #baby

Tags: [[Java Platform Cryptography and Security]]

# Java Cryptography Architecture

The Java Cryptography Architecture is a framework of Java APIs and providers for cryptographic services. It includes signatures, message digests, certificates, key generation and management, secure random-number generation, encryption, and key agreement through packages such as `java.security` and `javax.crypto`.

Its design separates an application's request for an algorithm from the code that implements it. An application obtains a [[JCA Engine Class]] instance by algorithm name, and a [[Cryptographic Service Provider]] supplies the selected implementation. This supports implementation independence, interoperability, and extensibility without requiring application developers to recreate cryptographic algorithms.

# References

[[cryptographyandcryptanalysisinjava.epub]]
