2026-10-18 16:30

Status: #baby

Tags: [[Cryptographic Randomness and Hashing]]

# Blum Blum Shub Generator

The Blum Blum Shub generator produces bits by repeatedly squaring a state modulo (n=pq), where (p) and (q) are suitably chosen primes, and taking a bit from each resulting state. Its unpredictability is tied to the difficulty of factoring the public modulus rather than to hiding the generator's algorithm.

Knowing a subsequence should not make the preceding or following bit practical to predict without the private factorization information. The construction prioritizes security over speed and is less efficient than many ordinary generators, illustrating the performance tradeoff inside [[Cryptographically Secure Random Number Generation]].

# References

[[cryptographyandcryptanalysisinjava.epub]]
