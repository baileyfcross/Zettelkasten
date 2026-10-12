2026-10-12 18:49

Status: #baby

Tags: [[Genetic Quantum Circuit Optimization]]

# GA4QCO Fidelity Benchmark

The GA4QCO fidelity benchmark uses ten randomly generated target circuits, each with four qubits and depth 20. For each target, the genetic search runs for 1,000 generations with a population of 200 circuits. An equal-budget random baseline creates the same number of random candidates per generation, and the results report mean best fitness, mean population fitness, and 95 percent confidence intervals across the ten targets.

In the unrestricted-gate experiment, both best and average fidelity improve over generations while the random baseline stays near its initial level; the mean best curve approaches roughly 0.8. Restricting the search to `id`, `rz`, `sx`, `x`, and `cx` produces a similar improving trend. Among the ten restricted runs, final best fidelity ranges from 0.67 to 0.994, compared with a highest random-baseline result of 0.79 and an average random-baseline fitness of 0.29.

The comparison shows evolutionary improvement over random generation for this particular small synthesis task. It does not compare against established circuit synthesis or architecture-search systems, quantify runtime or evaluation cost, include hardware noise, or test scaling beyond four qubits. The paper accordingly presents the benchmark as validation of the framework's approach, not evidence of practical superiority.

# References

[[2023 - GA4QCO Genetic Algorithm for Quantum Circuit Optimization.pdf]]
