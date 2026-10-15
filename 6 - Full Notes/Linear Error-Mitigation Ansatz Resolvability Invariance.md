2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Linear Error-Mitigation Ansatz Resolvability Invariance

Suppose the same affine mitigation map $C_m=a_1\widetilde C+a_2$ is applied to two noisy cost values. Their separation is multiplied by $a_1$, while the standard deviation of their estimators is multiplied by the same factor. The additive term cancels in the comparison, giving pairwise relative resolvability $\chi=1$ for any noise process.

The result means that a shared linear correction is neutral with respect to cost concentration: it neither reduces nor increases the shots needed to resolve those two points. Under global depolarizing noise, the optimal affine map can even correct every mean value exactly while leaving this finite-shot resolution unchanged.

Neutral resolvability does not mean the method is useless. By correcting [[Noise-Driven Cost Landscape Corruption]], a learned linear map can improve optimization when concentration is not dominant. Nor does the calculation include the samples required to learn the affine parameters.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
