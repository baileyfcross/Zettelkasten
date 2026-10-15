2026-10-15 00:05

Status: #baby

Tags: [[Quantum and Hybrid Convolutional Image Classification]]

# QAOA Encoding Expressibility-Trainability Tradeoff

QAOA-inspired encodings alternate feature-dependent rotations with nearest-neighbor $ZZ$ interactions. Changing the local-field axis changes the distribution of states they can generate. In the paper's frame-potential estimates, $X$- and $Y$-field variants lie closer to a Haar-random ensemble than the $Z$-field variant and are therefore more expressive by that measure.

The more expressive variants also showed larger performance variance in HQNN-Parallel, sometimes training well and sometimes failing, while the less expressive $Z$ variant was among the more stable encodings. The authors interpret this as an expressibility-trainability tradeoff: broad state coverage can place optimization in difficult regions instead of guaranteeing a useful representation. This is a numerical association from fixed random inputs and one benchmark, not a proof that the $Z$ field is generally preferable.

# References

[[2025 - Practical insights on the effect of different encodings ansatze and measurements in quantum and hybrid convolutional neural networks.pdf]]
