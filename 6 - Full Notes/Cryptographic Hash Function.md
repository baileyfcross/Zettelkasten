2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]]

# Cryptographic Hash Function

A cryptographic hash function maps data of arbitrary length to a fixed-size digest. The operation is designed to be one-way, and a useful secure hash makes it impractical to find a different input with the same digest.

Hashes can reveal whether data changed, but an unkeyed digest alone cannot establish who produced it because anyone can recompute the value. Password storage, message authentication, and digital signatures therefore build on hashing with additional mechanisms suited to each threat model.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
