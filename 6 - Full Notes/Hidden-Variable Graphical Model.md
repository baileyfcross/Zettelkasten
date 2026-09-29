2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Graphical Models]]

# Hidden-Variable Graphical Model

A hidden-variable graphical model accounts for influential variables that were not observed. Marginalizing a missing common cause can induce dependencies among many observed variables, so an originally sparse full graph may appear dense after the hidden node is removed.

This is a practical failure mode for sparse graph recovery. For example, an unmeasured regulator can connect many measured genes indirectly, making their observed precision structure look nonsparse. Interpreting a learned edge as a direct mechanism therefore requires considering latent causes and the measurement process, not only estimation error.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
