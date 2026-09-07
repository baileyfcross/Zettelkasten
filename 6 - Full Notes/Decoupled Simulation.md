2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Software Architecture]]

# Decoupled Simulation

Decoupled simulation separates application or world-state computation from the tracking and display processes that observe and render it. Each part can update at an appropriate rate and communicate through defined state or event interfaces.

The separation supports distribution, testing, and replacement of components, but it introduces synchronization work. The renderer must use a coherent simulation state and current pose rather than combining values from incompatible times.

# References

[[augmentedreality_pearson.pdf]]
