2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]]

# NISQ Quantum Medical Classification Scaling Limit

The medical-image experiments show a sharp gap between algorithmic scaling claims and usable NISQ scale. Five-qubit inner-product circuits tracked simulator outputs closely, but nine-qubit $[8,4,2]$ circuits produced many divergent values; end-to-end hardware training of that larger quantum-assisted model failed and predicted one class for the entire dataset.

Noise accumulated with circuit width and depth, and hardware behavior also varied across dates, qubit subsets, and machines. Unary postselection removed invalid bit strings but could not repair errors that remained inside the valid subspace. The study therefore concludes that contemporary hardware was not competitive with classical neural networks for medical-image classification, even though simulations supported the proposed asymptotic algorithms.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
