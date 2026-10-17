2026-09-13 20:16

Status: #baby

Tags: [[Emerging Computational Models]]

# Reversible Computing

Reversible computing uses operations whose inputs can be reconstructed uniquely from their outputs. By avoiding the routine erasure of information, it offers a theoretical route to reducing the energy dissipated by conventional computation.

Reversibility changes familiar programming assumptions because intermediate information cannot simply disappear. Algorithms and hardware must preserve enough state to undo each transformation.

The [[Quantum Circuit Model]] makes reversibility mandatory for closed-system gates: each operation is unitary and therefore has an inverse. Familiar irreversible functions are embedded in larger mappings that preserve inputs or work bits. A [[Toffoli Gate]], for example, computes $a\land b$ into a separate target without erasing either control.

# References

[[computationalthinking.epub]]
[[Introduction to Quantum Computing-NASA.pdf]]
