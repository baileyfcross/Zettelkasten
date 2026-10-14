2026-09-30 17:53

Status: #baby

Tags: [[Generative AI Model Adaptation and Serving]]

# NormalFloat Quantization

NormalFloat quantization assigns low-bit representation levels to match the approximately normal distribution often found in pretrained neural weights. The resulting nonuniform values preserve more useful resolution near dense portions of the distribution than uniformly spaced levels.

The four-bit NF4 format is commonly paired with [[Quantized Low-Rank Adaptation]]. Dequantization supplies values for computation while compact storage lowers memory pressure, creating a quality-versus-resource tradeoff that must be tested on the target task.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
