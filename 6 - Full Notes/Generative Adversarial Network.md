2026-09-30 21:11

Status: #baby

Tags: [[Deep Feature Representation]]

# Generative Adversarial Network

A generative adversarial network trains a generator and a discriminator against one another. The generator maps random inputs to candidate examples, while the discriminator learns to separate those generated examples from real training cases.

The generator improves by producing examples the discriminator classifies as real, and the discriminator improves as the generated counterexamples become harder. This coupled objective can learn a data distribution well enough to synthesize new cases, but the two-player training process is difficult to balance and generated quality may be harder to measure objectively than ordinary prediction error.

# References

[[machinelearning_mit.epub]]
