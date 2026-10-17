2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# Observable-Targeted MMD Regularization

Maximum mean discrepancy compares two sample distributions through kernel averages rather than an explicit density. For data samples $X$, generated samples $Y$, and kernel $k$, its squared empirical form combines within-$X$, within-$Y$, and cross-sample similarities:

$$\operatorname{MMD}^2=k(X,X)+k(Y,Y)-2k(X,Y).$$

Applying the comparison after a feature map lets training emphasize a scientifically important observable without replacing the global likelihood objective. The paper uses a Breit-Wigner kernel for the reconstructed $Z$-boson mass and Gaussian kernels otherwise, summing multiple bandwidths so the loss remains sensitive at several scales.

For a classical INN this loss mainly sharpens the targeted observable. In a QINN it also participates in the broader optimization role described by [[MMD-Guided QINN Training]].

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

