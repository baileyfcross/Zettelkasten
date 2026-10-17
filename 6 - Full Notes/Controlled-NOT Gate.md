2026-10-17 17:30

Status: #baby

Tags: [[Quantum Information and Circuit Foundations]]

# Controlled-NOT Gate

The controlled-NOT gate preserves a control qubit and flips a target qubit exactly when the control is $1$:

$$
|a,b\rangle\mapsto|a,a\oplus b\rangle.
$$

On basis values this resembles a reversible XOR. On superpositions it acts linearly and can create entanglement; applying it after a [[Hadamard Gate]] on the control transforms $|00\rangle$ into the Bell state $(|00\rangle+|11\rangle)/\sqrt2$. Its behavior is therefore not exhausted by its classical truth table.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

