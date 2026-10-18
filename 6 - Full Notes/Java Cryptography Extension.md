2026-10-18 16:30

Status: #baby

Tags: [[Java Platform Cryptography and Security]]

# Java Cryptography Extension

The Java Cryptography Extension supplies encryption, decryption, key generation, and key-agreement facilities through the `javax.crypto` family of packages. It includes the `Cipher` API, symmetric-key classes and specifications, initialization-vector specifications, and interfaces for algorithm-specific key types.

Within the [[Java Cryptography Architecture]], JCE complements the core `java.security` services. The book uses it for both symmetric and asymmetric transformations and identifies packages such as `javax.crypto.spec` for key and parameter objects. An application therefore requests a standardized service through Java APIs while a provider supplies the concrete implementation.

# References

[[cryptographyandcryptanalysisinjava.epub]]
