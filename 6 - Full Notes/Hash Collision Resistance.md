2026-10-18 16:30

Status: #baby

Tags: [[Cryptographic Randomness and Hashing]]

# Hash Collision Resistance

Hash collision resistance is the property that finding any two distinct inputs with the same digest should be computationally difficult. Collisions must exist when an arbitrarily large input space is compressed into a fixed-size output space, so the security claim is not that collisions are impossible; it is that locating one should require prohibitive work.

This differs from finding an input for a specified digest or finding a second input that matches one specified message. A [[Cryptographic Hash Function]] used for integrity or signatures needs its relevant resistance properties to hold against the attacker's actual freedom to choose messages.

# References

[[cryptographyandcryptanalysisinjava.epub]]
