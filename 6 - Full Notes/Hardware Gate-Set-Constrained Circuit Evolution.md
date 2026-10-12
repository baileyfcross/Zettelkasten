2026-10-12 18:49

Status: #baby

Tags: [[Genetic Quantum Circuit Optimization]]

# Hardware Gate-Set-Constrained Circuit Evolution

Hardware gate-set-constrained evolution limits the operations available to a circuit genome so every candidate is expressed in a specified basis. The restriction can reflect the gates physically implemented by a target device, preventing the evolutionary search from relying on operations that would later require separate decomposition.

GA4QCO demonstrates the idea with the set `id`, `rz`, `sx`, `x`, and `cx`. It reruns the fidelity search with the same population and generation settings used for unrestricted evolution. Across ten four-qubit targets, the final best individuals range from 0.67 to 0.994 fidelity; the highest random-baseline individual reaches 0.79 and the reported random-baseline average is 0.29.

This experiment establishes that a restricted alphabet can still support much better candidates than equal-budget random generation on the tested targets. It does not include device connectivity, calibrated gate error, or an executed hardware noise model, which the paper identifies as future extensions of [[Fidelity-Guided Quantum State Preparation Search]].

# References

[[2023 - GA4QCO Genetic Algorithm for Quantum Circuit Optimization.pdf]]
