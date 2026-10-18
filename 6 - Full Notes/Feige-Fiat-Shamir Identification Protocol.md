2026-10-18 16:30

Status: #baby

Tags: [[Public-Key Cryptosystems and Digital Identity]]

# Feige-Fiat-Shamir Identification Protocol

The Feige-Fiat-Shamir identification protocol is an interactive proof based on the difficulty of factoring a public modulus. In each round, the prover sends a randomized quadratic witness, the verifier returns a random bit-vector challenge, and the prover combines the round randomness with selected secret values to form a response. The verifier checks a modular-square relation against the witness and public values.

All rounds must pass before the identity is accepted. The security parameters govern both challenge size and repetition, so well-chosen values make successful impersonation unlikely. The protocol illustrates the completeness, soundness, and privacy goals in [[Zero-Knowledge Identification Properties]].

# References

[[cryptographyandcryptanalysisinjava.epub]]
