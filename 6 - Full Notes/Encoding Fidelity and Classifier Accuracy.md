2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Encoding Fidelity and Classifier Accuracy

Approximate state preparation is useful only if its errors preserve task-relevant distinctions. In the Fashion-MNIST experiments, increasing the number of encoding layers raises FRQI fidelity and generally improves downstream test accuracy, but deeper classifier circuits also contribute independently to accuracy.

The relationship is not one-to-one: average state overlap measures reconstruction across all amplitudes, whereas classification depends on boundaries between classes. Three sparse encoder layers reach 95.1% mean fidelity and support accuracy close to deeper general-ansatz encoders with substantially fewer CNOTs. This makes downstream validation necessary; a high state fidelity alone does not certify classification quality or hardware robustness.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
