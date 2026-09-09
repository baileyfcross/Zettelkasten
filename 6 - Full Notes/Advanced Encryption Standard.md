2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]]

# Advanced Encryption Standard

The Advanced Encryption Standard is a symmetric block cipher available through .NET cryptography APIs. It transforms fixed-size blocks under a secret key and is commonly combined with a mode of operation, padding rules, and an initialization value.

Security depends on more than selecting the AES algorithm name. Keys and initialization values must be generated and managed correctly, and applications should rely on established cryptographic constructions rather than inventing their own combinations of primitives.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
