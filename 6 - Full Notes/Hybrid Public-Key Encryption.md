2026-10-18 16:30

Status: #baby

Tags: [[Public-Key Cryptosystems and Digital Identity]]

# Hybrid Public-Key Encryption

Hybrid public-key encryption assigns different jobs to asymmetric and symmetric algorithms. A sender uses [[Asymmetric Encryption]] to protect a compact session key for the intended recipient, then uses [[Symmetric Encryption]] with that session key to protect the larger message body.

The arrangement combines the distribution advantage of a public key with the throughput of a shared-key cipher. The book uses secure Internet communication as the motivating pattern and later demonstrates the same division in [[Hybrid NTRU and AES Encryption]], where NTRU protects AES key material and AES processes the message. Security depends on authenticating the public key and protecting the generated session secret.

# References

[[cryptographyandcryptanalysisinjava.epub]]
