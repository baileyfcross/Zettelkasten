2026-10-15 00:14

Status: #baby

Tags: [[Quantum Computing for High-Energy Physics]]

# Quantum Rare-Signal Extraction in HEP

Rare-signal extraction in collider physics is an imbalanced classification problem: physically interesting events can be a tiny fraction of a much larger background. Accuracy is misleading in this setting because a model can score highly by ignoring the rare class. Precision-recall behavior, signal efficiency, background rejection, and prediction uncertainty are more informative.

Quantum proposals use variational classifiers, autoencoders, or quantum-kernel support-vector machines after classical dimensionality reduction. The hoped-for benefit is not simply a larger feature space; the circuit must learn a representation that improves discrimination or sample efficiency. Kernel concentration and barren plateaus can make nominally expressive models untrainable, while noise and repeated measurement add uncertainty.

Anomaly detection offers a model-agnostic alternative when no specific new-physics signal is known. The report cites early quantum autoencoder, quantum-kernel, and generative studies that matched or sometimes exceeded selected classical baselines at small scale, but it does not establish a systematic quantum advantage. A valid benchmark must use equally reduced data, strong classical comparators, rare-class metrics, and uncertainty estimates. [[HEP Quantum Machine Learning Data Reduction Pipeline]] defines the preprocessing that such comparisons inherit.

A focused [[Anomaly qGAN Framework|A-qGAN benchmark]] later learned a Standard Model background from 100 events and compared it with a parameter-matched classical GAN trained on 1,000. At seven PCA features their Graviton discrimination was comparable, while three-feature classical models remained better and repeated trials varied substantially. Because collider background data are abundant and the experiment did not use equal training-set sizes, the result is evidence of possible sample efficiency rather than a demonstrated operational advantage.

# References

[[2023 - Quantum Computing for High-Energy Physics State of the Art and Challenges Summary of the QC4HEP Working Group.pdf]]

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
