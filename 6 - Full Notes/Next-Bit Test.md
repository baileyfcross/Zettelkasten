2026-10-18 16:30

Status: #baby

Tags: [[Cryptographic Randomness and Hashing]]

# Next-Bit Test

The next-bit test asks whether an efficient observer who knows the first (k) output bits of a pseudorandom sequence, but not its seed, can predict bit (k+1) better than an unpredictable choice. A generator intended for cryptography should prevent such prediction.

The source presents the test as stronger than checking only visible frequencies: a generator that passes it also passes polynomial-time statistical tests for randomness. The criterion therefore connects output appearance to adversarial prediction and helps distinguish ordinary [[Pseudorandom Number Generation]] from [[Cryptographically Secure Random Number Generation]].

# References

[[cryptographyandcryptanalysisinjava.epub]]
