2026-10-18 16:30

Status: #baby

Tags: [[Quantum and Post-Quantum Cryptography]]

# NTRU Cryptosystem

NTRU is a public-key cryptosystem that works with low-coefficient polynomials in a truncated polynomial ring. Key generation chooses small polynomials and modular inverses; the public key combines those values modulo (q). Encryption mixes a message polynomial with the public key and a freshly chosen small random polynomial, while decryption uses the private polynomial and reductions modulo (q) and (p) to recover the message.

The source relates NTRU's hardness to a specialized [[Shortest Vector Problem]] and presents it as a [[Post-Quantum Cryptography|post-quantum]] candidate. Its Java example uses the scheme to protect compact symmetric material in [[Hybrid NTRU and AES Encryption]].

# References

[[cryptographyandcryptanalysisinjava.epub]]
