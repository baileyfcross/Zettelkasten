2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Per-Optimizer Learning-Rate Selection

Using the same numerical learning rate for different optimizers is not necessarily a fair comparison because their update directions and internal scaling differ. The optical study tunes vanilla gradient descent, natural-gradient descent, and Adam separately for each state-preparation task.

The appendix searches learning rates from $0.0001$ to $0.5$ using 20 random initializations. A rate is selected by trial and error for reaching a low loss quickly without excessive oscillation or eventual divergence.

This procedure avoids handicapping an optimizer with a clearly unsuitable shared rate, but it is still an empirical model-selection step. The displayed curves are representative around the selected values, and the search cost is not included in the final convergence comparison.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

