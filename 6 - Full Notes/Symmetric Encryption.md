2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]]

# Symmetric Encryption

Symmetric encryption uses the same secret key to encrypt plaintext and decrypt ciphertext. It is efficient for protecting substantial amounts of data, but every party that needs access must securely obtain and protect the shared key.

Confidentiality alone does not prove that encrypted data was not modified. A complete design must use an authenticated construction or pair encryption with appropriate integrity protection, while keeping keys separate from the data they protect.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
