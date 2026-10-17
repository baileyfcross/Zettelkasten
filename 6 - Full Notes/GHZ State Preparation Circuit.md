2026-10-17 17:30

Status: #baby

Tags: [[Quantum Information and Circuit Foundations]]

# GHZ State Preparation Circuit

An $n$-qubit Greenberger-Horne-Zeilinger state is

$$
|\mathrm{GHZ}_n\rangle=\frac{|0\cdots0\rangle+|1\cdots1\rangle}{\sqrt2}.
$$

It can be prepared from $|0\cdots0\rangle$ by applying a [[Hadamard Gate]] to one qubit and then using that qubit as the control for CNOTs targeting the remaining qubits.

The circuit scales with one Hadamard and $n-1$ controlled operations, whereas the equivalent full unitary has dimension $2^n\times2^n$. The construction demonstrates why gate-level descriptions remain compact even when the represented state space grows exponentially.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

