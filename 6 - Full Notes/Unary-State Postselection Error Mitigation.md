2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Unary-State Postselection Error Mitigation

Unary-state postselection exploits the invariant that a correctly executed unary-encoded circuit must produce a bit string with exactly one $1$. Measurement outcomes with zero or multiple excitations can therefore be discarded as invalid before estimating a neural-layer output.

This mitigation is efficient because it requires no detailed hardware-noise model, and it rejects common single bit-flip events that leave the intended subspace. It cannot detect every error: two coordinated flips can transform one valid unary string into another. The retained sample count also falls as noise grows, so postselection improves conditional accuracy without making deep noisy circuits reliable.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
