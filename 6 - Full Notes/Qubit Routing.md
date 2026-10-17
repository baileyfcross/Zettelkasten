2026-10-17 17:30

Status: #baby

Tags: [[Quantum Algorithm Execution and Verification]]

# Qubit Routing

Qubit routing maps a logical circuit onto hardware whose two-qubit gates act only on permitted physical connections. When two logical states must interact but occupy nonadjacent locations, the compiler inserts [[SWAP Gate|SWAPs]] or uses a swap network to move their states together.

Routing preserves logical semantics but increases depth and error exposure. Gate order, parallel execution, varying native durations, crosstalk, and noise can all affect the best route. For sets of commuting interactions, reordering provides additional freedom to reduce makespan.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

