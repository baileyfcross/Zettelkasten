2026-10-17 17:30

Status: #baby

Tags: [[Quantum Algorithm Execution and Verification]]

# Temporal Planning for Qubit Routing

Qubit routing can be formulated as a temporal-planning problem whose actions are native gates and state-moving operations, whose resources are physical qubits and couplers, and whose objective is minimum circuit makespan.

The planning model can include nearest-neighbor connectivity, unequal gate durations, and crosstalk restrictions. NASA experiments on interaction-heavy MaxCut QAOA circuits showed that general temporal planners were viable compilation tools, and later work combined planning with constraint programming. The formulation turns hardware details into explicit scheduling constraints instead of repairing connectivity greedily gate by gate.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

