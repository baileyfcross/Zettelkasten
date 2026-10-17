2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# QUBO Boolean Gate Encoding

A Boolean gate can be encoded as a QUBO whose minimum-energy rows are exactly the gate's valid truth-table assignments. Inputs and output receive binary variables, and invalid combinations receive positive penalties while valid combinations share the minimum objective value.

For NOT, one valid quadratic form is $2xy-x-y$, minimized when $y=\neg x$. OR and AND require three variables and carefully weighted invalid-row penalties so cubic terms cancel. The result turns local logical consistency into an energy condition that can be added to a larger circuit objective.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

