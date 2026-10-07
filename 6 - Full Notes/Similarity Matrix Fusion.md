2026-10-07 00:46

Status: #baby

Tags: [[Multi-Source Feature Selection]]

# Similarity Matrix Fusion

Similarity matrix fusion combines several local sample-similarity matrices into a global matrix, commonly through a weighted linear sum. Each local matrix represents the relationships inferred from one data or knowledge source.

The weights can be assigned by domain experts or learned from labels through a kernel-learning objective. The fused matrix can drive [[Spectral Feature Selection]], but incompatible scaling or an unreliable source can dominate unless matrices and weights are controlled carefully.

# References

[[spectralfeatureselectionfordatamining.pdf]]

