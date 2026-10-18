2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]] [[Cryptographic Randomness and Hashing]]

# Cryptographic Hash Function

A cryptographic hash function maps data of arbitrary length to a fixed-size digest. The operation is designed to be one-way, and a useful secure hash makes it impractical to find a different input with the same digest.

Hashes can reveal whether data changed, but an unkeyed digest alone cannot establish who produced it because anyone can recompute the value. Password storage, message authentication, and digital signatures therefore build on hashing with additional mechanisms suited to each threat model.

Integrity checking compares a newly computed digest with a trusted earlier digest: unchanged data should produce the same result. The source treats MD5 and SHA-1 as compromised choices and presents the SHA-2 family as their stronger successor for integrity applications.

The Java-focused source separates three attack goals. Preimage resistance makes it difficult to recover any input for a specified digest, second-preimage resistance makes it difficult to replace a known message with a different one having the same digest, and [[Hash Collision Resistance]] makes it difficult to find any colliding pair. It also contrasts legacy MD-family and SHA-1 designs with SHA-2 and SHA-3 constructions and describes attacks such as [[Length-Extension Attack|length extension]].

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[cybersecurity.epub]]

[[cryptographyandcryptanalysisinjava.epub]]
