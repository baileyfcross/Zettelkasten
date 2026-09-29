2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Image Quality Tier Selection

An adaptive image system can define a small number of quality tiers rather than expose every encoder setting. Slower or data-constrained contexts receive a smaller representation, while favorable contexts receive a higher-fidelity one.

The threshold should be derived from perceptual comparison such as SSIM or DSSIM and validated on representative content. Encoder quality numbers are not comparable across formats, so each tier is a visual and byte-budget target rather than a universal numeric setting. See [[Structural Similarity Index]].

# References

[[highperformanceimages.pdf]]
