2026-10-12 18:49

Status: #baby

Tags: [[Genetic Quantum Circuit Optimization]]

# Genetic Quantum Circuit Selection Pressure

Genetic quantum-circuit search applies selection twice: parent selection decides which circuits can reproduce, while survivor selection decides which candidates remain in the next generation. GA4QCO allows the same three methods to be configured independently for either role.

Random selection ignores fitness and therefore preserves exploration and genetic diversity, but it supplies no direct pressure toward the objective. Tournament selection repeatedly samples groups and returns the fittest circuit in each group. Roulette-wheel selection remains stochastic while giving a fitter circuit a higher probability of selection.

The choice determines how rapidly a population concentrates around currently successful circuits. Stronger fitness pressure can exploit useful gate patterns, whereas weaker pressure can retain material for [[Quantum Circuit Genome Crossover]] and [[Quantum Circuit Genome Mutation]] to explore. Because the paper's preliminary experiments report the resulting search rather than a controlled comparison of selection operators, it does not establish one method as generally superior.

# References

[[2023 - GA4QCO Genetic Algorithm for Quantum Circuit Optimization.pdf]]
