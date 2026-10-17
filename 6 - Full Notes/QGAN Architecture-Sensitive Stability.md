2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# QGAN Architecture-Sensitive Stability

QGAN training stability depends strongly on whether preprocessing and circuit structure encode the same constraints. The discrete copula circuit trained on probability-integral-transformed data shows smoother KL trajectories and fewer sudden jumps or mode-collapse-like failures than the standard min-max discrete circuit.

The continuous circuit does not show the same consistent PIT benefit. It uses an identical generic ansatz for both transformations and must learn uniform marginals rather than preserving them automatically, so changing the data alone does not provide the same inductive bias.

These observations are empirical and confounded by chosen hyperparameters, depth, and adversarial losses. They support architecture-data alignment as a stability hypothesis, not a universal result that PIT prevents QGAN collapse.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

