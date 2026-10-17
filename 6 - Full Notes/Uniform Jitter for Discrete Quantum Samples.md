2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Uniform Jitter for Discrete Quantum Samples

A discrete quantum generator selects one point on a finite grid. To produce apparently continuous values with a small register, the benchmark treats that point as the center of a cell and adds uniformly distributed classical noise within the cell.

Jitter increases the number of distinct numerical outputs beyond the circuit's $2^n$ basis states and makes plotted samples less concentrated at bin centers. It does not alter training or the quantum probability assigned to each cell.

The technique can accentuate discretization error because it assumes uniform density inside every selected cell. Fine sub-cell structure is invented by the postprocessor rather than learned, so [[Discrete Quantum Generator Grid Resolution]] still limits fidelity despite smoother-looking samples.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

