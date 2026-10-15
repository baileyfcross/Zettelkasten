2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# Quantum Encoding Placement Tradeoff

An encoding that works on a compressed global feature vector may fail when applied independently to small raw-image patches. Amplitude encoding illustrates the difference: it was effective in the quantum-later HQNN-Parallel model but among the weakest encodings in the early quanvolutional model.

Patchwise amplitude normalization can dilute magnitude and contrast information that an initial feature extractor needs to preserve. Single-qubit rotation encodings maintain a more local feature-to-qubit correspondence and were robust in both placements. The result makes circuit location part of encoding design. Global compression favors qubit-efficient representations such as [[Amplitude Encoding for Circuit-Centric Classification]], while a local front end benefits from a map whose normalization and entangling pattern do not erase distinctions inside each receptive field.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
