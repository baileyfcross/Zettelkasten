2026-09-29 19:17

Status: #baby

Tags: [[High-Dimensional Inference and Multiple Testing]]

# Step-Up Multiple Testing Procedure

A step-up multiple testing procedure orders p-values and finds the largest rank whose p-value is below a rank-dependent threshold. It then rejects every hypothesis up through that rank.

Unlike a fixed cutoff applied independently, the boundary can become less stringent as more small p-values accumulate. The procedure must be analyzed as a whole because the number of rejections is random and depends on all tests. Both the [[Benjamini-Hochberg Procedure]] and the [[Benjamini-Yekutieli Procedure]] use this structure with different thresholds and dependence guarantees.

# References

[[introductiontohigh-dimensionalstatistics.pdf]]
