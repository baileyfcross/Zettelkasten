2026-10-12 18:49

Status: #baby

Tags: [[Genetic Quantum Circuit Optimization]]

# GA4QCO Quantum Circuit Optimization Framework

GA4QCO is a toolbox for using a [[Genetic Algorithm Search|genetic algorithm]] to construct new quantum circuits or optimize existing ones for user-defined properties. A population of encoded circuits evolves through parent selection, crossover, mutation, fitness evaluation, and survivor selection; the highest-fitness individual after the configured generations is returned as the candidate circuit.

The user controls circuit width and depth, population size, generation count, variation probabilities, selection operators, the allowed gate set, and the fitness function through a property configuration. This separates the evolutionary machinery from the search objective, allowing the same framework to target fidelity, entanglement, classification or regression accuracy, circuit size, or combinations of these properties.

The paper demonstrates feasibility rather than scalability or quantum advantage. Its experiments use simulation, four qubits, depth-20 targets, and fidelity objectives. Noise-aware fitness, larger circuits, stronger comparisons with other architecture-search methods, and more advanced objectives are left for future work.

# References

[[2023 - GA4QCO Genetic Algorithm for Quantum Circuit Optimization.pdf]]
