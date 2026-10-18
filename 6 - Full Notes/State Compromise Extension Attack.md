2026-10-18 16:30

Status: #baby

Tags: [[Cryptographic Randomness and Hashing]]

# State Compromise Extension Attack

A state compromise extension attack begins when an adversary learns a pseudorandom generator's internal state, even temporarily, and then tries to extend that disclosure into knowledge of other outputs. The attacker may seek earlier values, later values, or enough structural information to continue predicting the sequence after the immediate compromise is repaired.

Resistance means that disclosure of one state or subsequence does not automatically reveal the entire stream. This is a security property beyond ordinary distribution tests and is particularly important when generated values become keys, session identifiers, or authentication codes through [[Cryptographically Secure Random Number Generation]].

# References

[[cryptographyandcryptanalysisinjava.epub]]
