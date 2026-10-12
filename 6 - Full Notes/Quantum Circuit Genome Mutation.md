2026-10-12 18:49

Status: #baby

Tags: [[Genetic Quantum Circuit Optimization]]

# Quantum Circuit Genome Mutation

Quantum-circuit genome mutation introduces structural or parametric variation after crossover. GA4QCO applies mutation probabilistically to new children so the population can explore circuits that are not direct recombinations of the current parents.

Its single-gate flip replaces a selected gate and consistently replaces every cell affected by a selected multi-qubit gate. Other structural operators swap two depth columns, reverse the control and target of a controlled gate, add or remove a qubit, or add and remove gates across qubit wires. A parameter mutation instead changes the angle of a randomly selected parameterized gate.

These operators span local gate choice, scheduling, interaction direction, circuit width, circuit depth, and continuous parameters. Their usefulness depends on the [[Quantum Circuit Genome Encoding]] and allowed gate set: a mutation must produce an executable individual even when it changes a multi-qubit operation or a circuit dimension.

# References

[[2023 - GA4QCO Genetic Algorithm for Quantum Circuit Optimization.pdf]]
