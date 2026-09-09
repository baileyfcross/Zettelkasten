2026-09-08 21:16

Status: #baby

Tags: [[ML.NET Recommendation Applications]]

# ML.NET Data Preparation

ML.NET data preparation converts raw columns into values an algorithm can learn from. Common steps include replacing missing values, mapping categorical values to keys, normalizing numeric inputs, and combining selected columns into a feature vector.

Preparation choices become part of the model's semantics, not merely cleanup. They must be fitted on training data and replayed consistently for evaluation and production predictions to avoid leakage or incompatible inputs.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
