2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Metric-Inversion Scaling for Multimode Optical Circuits

Counting a complex coordinate as two real degrees of freedom, a generic $N$-mode Gaussian optical layer has an effective parameter count

$$n=2N^2+4N.$$

Its natural-gradient metric is $n\times n$, so a dense inversion has classical cost $O(n^3)=O(N^6)$. Computing one full metric over many layers would increase the dimension further.

This scaling motivates [[Layerwise Block-Diagonal Quantum Natural Gradient|layerwise block-diagonal metrics]]. The single-mode experiments use blocks no larger than $6\times6$, where inversion is negligible, but that runtime observation cannot be extrapolated directly to large multimode circuits.

Natural gradient can reduce the number of optimization steps while increasing the work per step. Practical advantage depends on both quantities and on the cost of estimating the metric entries.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

