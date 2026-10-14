2026-09-30 17:53

Status: #baby

Tags: [[Generative AI Model Adaptation and Serving]]

# Blockwise Quantization

Blockwise quantization divides a large weight tensor into smaller groups and calculates quantization parameters separately for each group. Local scales reduce the distortion caused when one global range must represent values with different distributions.

Smaller blocks can preserve more information but require more scale metadata and processing. In QLoRA-style adaptation, blockwise low-bit storage helps a frozen base model fit in memory while higher-precision computation trains the adapter.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
