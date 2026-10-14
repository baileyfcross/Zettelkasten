2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Fashion-MNIST Quantum Classifier Hardware Benchmark

The benchmark encodes all 70,000 Fashion-MNIST images as 11-qubit [[Flexible Representation of Quantum Images|FRQI states]], trains 42 ten-class classifier configurations in noiseless simulation, and deploys their combined encoding-classification circuits on ibmq-kolkata. Training and state preparation optimization occur classically; only inference circuits run on the quantum processor.

Noiseless test accuracy on all 10,000 test images rises from roughly the high-50s into the low-80% range as encoding and classifier resources grow, below the 89.48% exact-FRQI quadratic-kernel SVM reference. Hardware evaluation is limited to the first 100 test images with 100,000 shots each and peaks around 40%; deeper CNOT-heavy circuits frequently approach the ten-class random baseline.

The result demonstrates that a standard full-dimensional image dataset can be approximately encoded and processed on current hardware. It does not show competitive Fashion-MNIST performance, efficient quantum training, or quantum advantage.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
