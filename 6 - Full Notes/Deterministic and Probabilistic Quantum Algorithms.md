2026-10-17 17:30

Status: #baby

Tags: [[Quantum Algorithm Execution and Verification]]

# Deterministic and Probabilistic Quantum Algorithms

Quantum computation is not inherently probabilistic at the algorithm level. A quantum computer can implement a deterministic classical computation with the same certainty, and interference can make a quantum algorithm return a definite result even though intermediate states are superpositions.

Other algorithms intentionally use random choices or measurements and succeed with a stated probability. Shor's factoring algorithm is randomized, whereas variants of Grover search can preserve the quadratic speedup while returning the marked item with certainty when the problem size is known. Probability is therefore an algorithm property, not a universal consequence of using qubits.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

