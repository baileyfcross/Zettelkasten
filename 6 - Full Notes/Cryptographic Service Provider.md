2026-10-18 16:30

Status: #baby

Tags: [[Java Platform Cryptography and Security]]

# Cryptographic Service Provider

A cryptographic service provider is a Java package or group of packages that implements cryptographic services such as signatures, digests, ciphers, and key-management algorithms. Installed providers publish their names, supported algorithms, and service implementations to the [[Java Cryptography Architecture]].

An application can request an algorithm without naming a provider and let the framework search the installed order, or it can request a specific provider when that implementation matters. Providers make the framework extensible, but third-party implementations still require testing, standardization review, and careful compatibility checks rather than automatic trust merely because they plug into the same API.

# References

[[cryptographyandcryptanalysisinjava.epub]]
