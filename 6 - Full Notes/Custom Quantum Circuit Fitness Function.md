2026-10-12 18:49

Status: #baby

Tags: [[Genetic Quantum Circuit Optimization]]

# Custom Quantum Circuit Fitness Function

A custom quantum-circuit fitness function maps each candidate circuit to a scalar that expresses the user's optimization goal. It may combine the number of gates, properties of the prepared state, performance after variational training, and hardware-related constraints, with the user choosing how the components are weighted.

GA4QCO provides examples for state fidelity, entanglement measured by von Neumann entropy, and machine-learning accuracy. For classification or regression, each circuit undergoes an inner learning process that adjusts its parameterized gates on the dataset; training accuracy after a fixed number of learning steps becomes the circuit's evolutionary fitness.

This design makes the search framework reusable but moves responsibility for the desired behavior into the objective. A poorly weighted scalar can reward an unintended compromise, while an expensive inner training loop can make evaluating a population costly. [[Fidelity-Guided Quantum State Preparation Search]] illustrates the paper's experimentally evaluated objective.

# References

[[2023 - GA4QCO Genetic Algorithm for Quantum Circuit Optimization.pdf]]
