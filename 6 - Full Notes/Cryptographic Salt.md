2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]] [[Applied Cryptography and PKI]]

# Cryptographic Salt

A cryptographic salt is random data combined with a password before deriving or hashing its stored verifier. A distinct salt causes identical passwords to produce different results and frustrates precomputed lookup tables.

The salt can be stored with the derived value because its purpose is uniqueness, not secrecy. It should be generated independently for each password with a cryptographically secure random source and used with a deliberately expensive password-derivation function.

In password authentication, a pseudorandom salt is attached to the password before its stored verifier is calculated. An attacker who guesses the human-selected password must still account for the stored salt, and identical passwords no longer share one reusable digest.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[cybersecurity.epub]]
