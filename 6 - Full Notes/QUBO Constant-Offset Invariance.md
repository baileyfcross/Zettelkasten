2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# QUBO Constant-Offset Invariance

Adding or removing a constant from every value of a QUBO objective shifts all energies equally and does not change which binary assignments minimize it. If $O'(x)=O(x)+c$, then $O'(x_1)<O'(x_2)$ exactly when $O(x_1)<O(x_2)$.

Constant terms can therefore be discarded when a quantum annealer is used only to identify minimizers. They must be retained when the absolute objective value has an external meaning or when results from independently normalized formulations are compared.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

