2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# QAOA Phase Separator

A QAOA phase separator is a unitary whose eigenphases encode the classical objective value. For a diagonal cost Hamiltonian $H_P$ satisfying $H_P|z\rangle=C(z)|z\rangle$, one layer applies

$$
U_P(\gamma)=e^{-i\gamma H_P}.
$$

The operation does not change computational-basis probabilities by itself; it writes cost-dependent relative phases into the superposition. A following [[QAOA Mixing Operator]] turns those phase differences into changed amplitudes, allowing interference to favor better assignments.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

