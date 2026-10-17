2026-09-13 20:16

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# Quantum Annealing as Computation

Quantum annealing encodes an optimization problem into an energy landscape and lets a quantum system settle toward a low-energy state. The measured state is then interpreted as a candidate solution.

Programming this machine means configuring coefficients and constraints rather than specifying a sequence of instructions. Its usefulness depends on whether the problem can be mapped faithfully to the supported physical model.

The computation begins in the ground state of an easily prepared driver Hamiltonian and changes toward a problem Hamiltonian whose low-energy configurations encode preferred answers. Practical quantum annealing uses repeated finite-time runs and may exploit both quantum and thermal transitions; it should not be conflated with an ideal infinitely slow adiabatic process.

# References

[[computationalthinking.epub]]
[[Introduction to Quantum Computing-NASA.pdf]]
