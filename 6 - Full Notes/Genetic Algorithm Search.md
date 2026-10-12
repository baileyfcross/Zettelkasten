2026-09-13 20:16

Status: #baby

Tags: [[Computational Science and Simulation]] · [[Genetic Quantum Circuit Optimization]]

# Genetic Algorithm Search

A genetic algorithm searches with a population of candidate solutions encoded in a manipulable representation. A fitness function selects promising candidates, while mutation and crossover generate a new population for the next iteration.

Repeated selection often finds good solutions to optimization problems whose exhaustive search is intractable. The result is heuristic: success depends on representation, fitness, diversity, and the available computational budget.

The representation and variation operators must preserve the structure of the problem being searched. In quantum-circuit design, for example, [[Quantum Circuit Genome Encoding]] records gates across qubit rows and circuit-depth columns, while circuit-aware crossover and mutation repair or consistently replace the metadata belonging to multi-qubit gates.

# References

[[computationalthinking.epub]]
[[2023 - GA4QCO Genetic Algorithm for Quantum Circuit Optimization.pdf]]
