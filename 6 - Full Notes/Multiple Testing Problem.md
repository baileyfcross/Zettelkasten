2026-09-14 20:21

Status: #baby

Tags: [[High-Dimensional Inference and Multiple Testing]]

# Multiple Testing Problem

The multiple testing problem arises when many hypotheses are examined simultaneously. Even if every null hypothesis is true, applying the same per-test p-value cutoff repeatedly can produce one or more false positives with high probability.

High-throughput inference therefore defines a selection procedure and controls an error rate for the resulting list. [[Family-Wise Error Rate]] and [[False Discovery Rate]] express different tolerances for mistakes and lead to different discovery power.

If $m_0$ null hypotheses are true and each is tested at level $\alpha$, the expected number of false positives is $\alpha m_0$. This can exceed the number of genuine effects when $m_0$ is large, even though every individual test is correctly calibrated. Multiplicity is therefore an accumulation problem, not a defect in the single-test p-value.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
