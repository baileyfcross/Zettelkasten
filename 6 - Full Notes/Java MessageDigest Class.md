2026-10-18 16:30

Status: #baby

Tags: [[Java Platform Cryptography and Security]]

# Java MessageDigest Class

Java's `MessageDigest` engine computes an unkeyed digest with an algorithm supplied by a security provider. The application obtains an instance for a named algorithm, feeds it message bytes, and requests the final fixed-size result. The book converts the returned bytes to hexadecimal for display and applies the same process to file integrity checking.

The class provides access to a [[Cryptographic Hash Function]], but it does not turn that digest into authentication. If an attacker can replace both a file and its untrusted digest, recomputation proves nothing about origin. A [[Message Authentication Code]] or [[Digital Signature]] adds the key-based evidence required for that different claim.

# References

[[cryptographyandcryptanalysisinjava.epub]]
