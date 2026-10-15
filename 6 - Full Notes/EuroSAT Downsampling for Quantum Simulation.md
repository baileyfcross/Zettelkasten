2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# EuroSAT Downsampling for Quantum Simulation

EuroSAT contains 27,000 balanced, georeferenced Sentinel-2 images across ten land-cover classes, with RGB inputs at $64\times64$ pixels. To make quantum-circuit simulation tractable, the study downsamples RGB images to $32\times32$ and $16\times16$. Reported structural similarity remains above 0.90 and 0.78, respectively, relative to the original resolution.

Only the hybrid models use the 32-pixel version; both hybrid and fully quantum models use the 16-pixel version because the latter must encode the entire image within roughly 10 to 15 qubits. The reduction preserves enough texture for the controlled comparison while changing the task from full-resolution remote-sensing classification. The benchmark therefore treats downsampling as a NISQ-era simulation constraint, and its observed resolution insensitivity should be interpreted within those two compressed scales.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
