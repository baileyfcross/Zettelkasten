2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Quantum Rare-Signal Extraction in HEP

Rare-signal extraction in collider physics is an imbalanced classification problem: physically interesting events can be a tiny fraction of a much larger background. Accuracy is misleading in this setting because a model can score highly by ignoring the rare class. Precision-recall behavior, signal efficiency, background rejection, and prediction uncertainty are more informative.

Quantum proposals use variational classifiers, autoencoders, or quantum-kernel support-vector machines after classical dimensionality reduction. The hoped-for benefit is not simply a larger feature space; the circuit must learn a representation that improves discrimination or sample efficiency. Kernel concentration and barren plateaus can make nominally expressive models untrainable, while noise and repeated measurement add uncertainty.

Anomaly detection offers a model-agnostic alternative when no specific new-physics signal is known. The report cites early quantum autoencoder, quantum-kernel, and generative studies that matched or sometimes exceeded selected classical baselines at small scale, but it does not establish a systematic quantum advantage. A valid benchmark must use equally reduced data, strong classical comparators, rare-class metrics, and uncertainty estimates. [[HEP Quantum Machine Learning Data Reduction Pipeline]] defines the preprocessing that such comparisons inherit.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]
