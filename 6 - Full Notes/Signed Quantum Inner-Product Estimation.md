2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Signed Quantum Inner-Product Estimation

Signed quantum inner-product estimation loads a normalized input $x$ and then applies the adjoint loader for a normalized weight vector $w$. Measuring the first qubit in the basic circuit estimates $(w\cdot x)^2$, which loses the sign and is insufficient for neural weights that may contain negative components.

The signed construction adds one qubit and a constant number of gates. Interference changes the relevant amplitude to $(1-w\cdot x)/2$, a nonnegative quantity from which $w\cdot x$ can be reconstructed after repeated computational-basis measurements. This makes the circuit usable as the arithmetic primitive in a [[Quantum-Assisted Neural Network]] without assuming positive weights or inputs.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
