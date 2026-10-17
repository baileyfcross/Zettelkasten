2026-10-17 17:30

Status: #baby

Tags: [[Constraint-Preserving QAOA]]

# Quantum Alternating Operator Ansatz

The quantum alternating operator ansatz prepares a feasible initial state and alternates problem-phase and mixing unitaries for $p$ layers:

$$
|\boldsymbol\beta,\boldsymbol\gamma\rangle=
U_M(\beta_p)U_P(\gamma_p)\cdots U_M(\beta_1)U_P(\gamma_1)|s\rangle.
$$

A classical optimizer chooses the $2p$ angles from measured objective estimates. The formulation generalizes the original approximate-optimization algorithm by permitting mixers that are not a single transverse-field evolution and by targeting exact optimization or sampling as well as approximation.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

