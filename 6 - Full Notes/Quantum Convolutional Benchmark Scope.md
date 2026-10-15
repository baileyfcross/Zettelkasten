2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Quantum Convolutional Benchmark Scope

The study is a controlled design sweep rather than a claim of state-of-the-art accuracy or quantum utility. It evaluates about 500 combinations of encodings, ansatzes, measurements, image sizes, and circuit layouts on 500 EuroSAT examples with an 80:20 split. Configurations share optimizer and data settings so component effects can be compared, but most specific combinations are executed only once.

All results come from ideal PennyLane simulations connected to PyTorch classical layers. The benchmark fixes optimization hyperparameters, omits a systematic gradient-variance study, uses one dataset, and does not model device noise or hardware execution time. Initial sensitivity tests suggested low initialization variance, yet the reported rankings can still depend on the restricted component menu and training regime. The conclusions are practical hypotheses about architecture selection that require replication on other datasets, noise models, and physical devices.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
