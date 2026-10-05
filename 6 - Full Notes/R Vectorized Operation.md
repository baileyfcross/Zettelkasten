2026-10-04 22:20

Status: #baby

Tags: [[R Data Transformation and Reshaping]]

# R Vectorized Operation

An R vectorized operation applies arithmetic, logical, summary, or transformation behavior across an entire vector rather than requiring an explicit loop for each element. Operations align elements positionally and may recycle shorter operands, so unequal lengths can produce a valid-looking result that does not represent the intended pairing.

Vectorization makes transformations concise, but missing values and type coercion remain part of the computation. The analyst should decide whether missing values propagate or are removed and verify that the resulting vector still aligns with its source observations.

# References

[[rprimer.pdf]]
