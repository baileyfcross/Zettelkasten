2026-10-18 16:30

Status: #baby

Tags: [[Public-Key Cryptosystems and Digital Identity]]

# RSA Cryptosystem

RSA is a public-key cryptosystem whose key generation begins with two distinct large primes (p) and (q). Their product (n) is paired with a public exponent (e); a private exponent (d) is selected as the modular inverse of (e) relative to the totient derived from the primes. Encryption raises a message representation to (e) modulo (n), and decryption applies the private exponent.

Its security is tied to the difficulty of recovering the private information from the public modulus. Implementations must also address timing leakage and chosen-ciphertext behavior rather than relying on factorization difficulty alone. RSA is one example of [[Asymmetric Encryption]].

# References

[[cryptographyandcryptanalysisinjava.epub]]
