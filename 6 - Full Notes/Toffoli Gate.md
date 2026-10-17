2026-10-17 17:30

Status: #baby

Tags: [[Quantum Information and Circuit Foundations]]

# Toffoli Gate

The Toffoli, or controlled-controlled-NOT, gate maps

$$
|a,b,c\rangle\mapsto|a,b,c\oplus ab\rangle.
$$

It flips the target only when both controls are $1$, while preserving all three wires and remaining reversible.

Toffoli gates can implement arbitrary classical Boolean functions when constants and retained work bits are available. For example, a target initialized to $0$ receives $a\land b$, while a target initialized to $1$ receives the NAND of the controls. This makes Toffoli a bridge between irreversible Boolean descriptions and reversible circuits.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

