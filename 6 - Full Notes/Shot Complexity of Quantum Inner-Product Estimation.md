2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# Shot Complexity of Quantum Inner-Product Estimation

An inner-product circuit produces a sample rather than an exact scalar. Estimating its measurement probability to additive error $\epsilon$ with high probability requires $O(1/\epsilon^2)$ circuit repetitions, so the ideal gate depth cannot be treated as the entire running time.

With a parallel [[Unary Quantum Data Loader Topologies|unary data loader]], one shot can have logarithmic depth in the feature dimension, but the shot multiplier and physical gate time remain. The paper used 400 repetitions as an empirically adequate precision setting and explicitly cautions that a crossover in abstract step counts against one CPU does not imply a speed advantage over optimized GPU or TPU matrix multiplication.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
