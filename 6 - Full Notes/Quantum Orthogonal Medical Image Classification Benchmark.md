2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]] · [[Biomedical Image Analysis]]

# Quantum Orthogonal Medical Image Classification Benchmark

The quantum-orthogonal benchmark compares $[4,2]$ and $[8,2]$ classifiers trained with the pyramid-angle algorithm against classical singular-value-bounding orthogonal networks. On the main four- and eight-feature Pneumonia-MNIST and Retina-MNIST tests, simulator results are generally close to the classical baselines, and hardware inference usually incurs a modest drop.

The optimization landscape can nevertheless produce different models even when both parameterizations represent orthogonal matrices. In a larger simulated $[32,16,2]$ retinal example, [[RBS Angle-Space Backpropagation]] reached 75.25% test accuracy while singular-value bounding collapsed toward one class at 58.25%. This is an example of a favorable training outcome, not proof that the quantum parameterization is consistently superior.

The hardware circuits use only four or eight PCA features and no hidden layer because deeper orthogonal circuits exceeded practical device quality. Their results demonstrate executability and approximate agreement with simulation rather than diagnostic readiness or quantum advantage.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
