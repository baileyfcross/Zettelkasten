2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Generative Generalization Tradeoffs

The benchmark separates the ability to explore, remain valid, improve objective value, and cover many distinct improvements. Models that perform well on one axis can perform poorly on another, so an aggregate claim of “better generation” is underspecified without the application priority.

The VAE and WGAN achieve the strongest quality results in the larger-data regime but show weaker exploration, validity, and normalized coverage, consistent with concentrated or collapsed outputs. The RNN and Transformer retain relatively strong validity but their low-cost generalization can deteriorate during training. The QCBM supplies the most balanced validity-quality profile in the scarce-data setting.

These tradeoffs explain why [[Generative Model Advantage Race Design]] must select metrics and resource limits in advance. A model optimized for one track can lose another without contradiction, and a practical advantage exists only relative to the bottleneck that matters to the use case.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

