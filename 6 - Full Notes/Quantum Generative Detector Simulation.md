2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Quantum Generative Detector Simulation

Detailed Monte Carlo detector simulation consumes a major share of collider-computing resources, and higher-granularity future detectors increase that burden. A quantum generative model seeks to learn the multidimensional detector-response distribution and produce synthetic events more cheaply, using architectures such as quantum GANs, quantum autoencoders, or quantum circuit Born machines.

Near-term implementations are limited by output dimension and resolution. A direct mapping can consume one qubit per detector sensor, restricting experiments to tiny arrays. A hybrid alternative compresses detector output with a classical encoder, trains the quantum generator on the latent distribution, and expands generated samples with a classical decoder. The quantum model's quality then depends on what the classical bottleneck preserves.

Continuous energy deposits must also be discretized for qubit-based generation, and realistic samples require correct correlations and diversity rather than only plausible individual images. Generating analysis-level particle features is smaller than reproducing raw detector output but creates an analysis-specific model that cannot be reused freely. Evaluation must therefore separate speed, fidelity, coverage, reconstruction compatibility, and classical preprocessing cost. [[HEP Quantum Machine Learning Data Reduction Pipeline]] provides the general hybrid pattern.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
