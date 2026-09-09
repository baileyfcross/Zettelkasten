2026-09-08 21:16

Status: #baby

Tags: [[.NET Cryptography and Access Control]]

# SHA-256 Hashing

SHA-256 is a member of the SHA-2 family that produces a 256-bit digest. .NET exposes implementations that can hash a byte array or stream, allowing large content to be processed without loading it all at once.

The digest is often encoded as hexadecimal or Base64 for storage and comparison. SHA-256 is suitable for content integrity and as a component in established constructions, but fast general-purpose hashing by itself is not an adequate password-storage scheme.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
