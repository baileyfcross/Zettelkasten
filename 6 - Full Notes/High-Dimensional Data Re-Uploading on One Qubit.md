2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# High-Dimensional Data Re-Uploading on One Qubit

Ansatz A inserts an arbitrary-dimensional feature vector into one rotation angle through the learned projection $\omega\cdot x+\alpha$. The number of input features therefore does not force the quantum register to grow: a single physical qubit can receive two-, three-, or four-dimensional samples through its control parameters.

Constant width does not mean constant difficulty. Compressing more coordinates into each rotation can make the required feature-to-state map harder to represent with a fixed number of layers. In the four-layer experiments, accuracy falls from 93 percent on the two-dimensional circle to 66 percent on the three-dimensional sphere and 64 percent on the four-dimensional hypersphere before device fine-tuning.

The paper identifies more re-uploading layers or a richer encoding with additional degrees of freedom as remedies. [[Single-Qubit Re-Uploading Universality]] describes the asymptotic representational claim, whereas this result shows the limitations of a finite-depth implementation.

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
