2026-10-14 17:27

Status: #baby

Tags: [[Unary-Encoded Quantum Neural Networks]] · [[Biomedical Image Analysis]]

# Quantum-Assisted Medical Image Classification Benchmark

The quantum-assisted benchmark classifies pediatric chest radiographs from Pneumonia-MNIST and retinal fundus images from Retina-MNIST. Because the available processors could not load all 784 pixels, principal-component analysis reduced each image to four or eight features before training $[4,4,2]$ or $[8,4,2]$ networks.

Simulator-based [[Quantum-Assisted Neural Network|quantum-assisted networks]] closely matched the corresponding classical networks. For the eight-feature model, test accuracy was 83% versus 85% classically on pneumonia and 80% versus 78% classically on retina; these small differences do not establish an advantage. On hardware, simulator-trained inference remained close for several configurations, but training and inference of the four-feature retinal model fell to 60% accuracy.

The comparison is a proof of concept on heavily compressed binary tasks, not evidence that quantum hardware improves clinical diagnosis. The data reduction, small network widths, finite-shot estimation, and single hardware runs limit the interpretation of the reported accuracy.

# References

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
