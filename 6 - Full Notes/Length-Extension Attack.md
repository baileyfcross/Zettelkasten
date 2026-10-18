2026-10-18 16:30

Status: #baby

Tags: [[Cryptographic Randomness and Hashing]]

# Length-Extension Attack

A length-extension attack uses the digest of an unknown message together with that message's length to compute a valid digest for the original message followed by attacker-chosen data, without first recovering the original message. The attack targets how some iterative hash constructions expose their final internal state.

It shows why an unkeyed digest should not be treated as a [[Message Authentication Code]]. Authentication must use a construction designed around a secret key, because simply placing a secret next to a vulnerable iterative hash can leave the composition open to extension even when the hash remains difficult to invert.

# References

[[cryptographyandcryptanalysisinjava.epub]]
