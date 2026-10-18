2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]] [[Cryptographic Randomness and Hashing]] [[Java Platform Cryptography and Security]]

# Cryptographically Secure Random Number Generation

Security-sensitive values require randomness that an attacker cannot feasibly predict. .NET cryptographic random-number generators draw from operating-system facilities intended for keys, salts, nonces, and other secrets.

The ordinary `Random` class is useful for simulation and general variation but is not designed to resist prediction. Choosing the cryptographic generator is therefore a security boundary, not merely a matter of producing a wider range of numbers.

The Java source makes the same distinction between general pseudorandom interfaces and `java.security.SecureRandom`. It describes operating-system random data as the seed material for `SecureRandom`, contrasts that with ordinary time-derived seeding, and recommends the secure generator for keys, one-time passwords, and session identifiers whose predictability would enable impersonation or guessing.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[cryptographyandcryptanalysisinjava.epub]]
