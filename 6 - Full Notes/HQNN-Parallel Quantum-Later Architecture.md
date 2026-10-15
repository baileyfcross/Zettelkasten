2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# HQNN-Parallel Quantum-Later Architecture

HQNN-Parallel is a quantum-later hybrid architecture: classical convolutions first extract image features, and parameterized quantum circuits operate only after the feature maps have been flattened. A final classical stage turns the measured quantum outputs into class probabilities. The quantum component therefore receives a compressed, learned representation rather than raw pixels.

In the EuroSAT study, the classical feature extractor is adjusted so both $32\times32$ and $16\times16$ inputs produce a 768-element vector. That fixed interface supports the same [[Parallel Quantum Linear Layer]] across resolutions. The best reported 32-pixel hybrid configuration reached 75.1% validation accuracy with IQP encoding and a non-entangling ansatz, compared with 67.1% for its controlled classical baseline. Both models nevertheless began to overfit after only a few epochs, so the comparison does not imply unrestricted gains from longer training.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
