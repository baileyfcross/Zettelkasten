2026-10-18 16:30

Status: #baby

Tags: [[Privacy-Preserving Encryption]]

# Searchable Encryption

Searchable encryption lets a server search encrypted documents without first decrypting the stored collection. A data owner encrypts documents and prepares an index, a data user transforms a keyword query into a protected search value, and the server applies that value to the encrypted index before returning encrypted matches for user-side decryption.

Schemes may use one private key for all operations or divide roles between public and private keys. Security also requires controlled query authorization, encrypted query material, and [[Search Query Isolation]] so the server does not learn unnecessary relationships among keywords, documents, and results.

# References

[[cryptographyandcryptanalysisinjava.epub]]
