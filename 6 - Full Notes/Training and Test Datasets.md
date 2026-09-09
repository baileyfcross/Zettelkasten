2026-09-08 21:16

Status: #baby

Tags: [[ML.NET Recommendation Applications]]

# Training and Test Datasets

Training data is used to fit a model's parameters, while test data is withheld to estimate how the learned model behaves on unseen examples. Evaluating on the same observations used for fitting gives an overly optimistic picture of generalization.

The split must preserve the structure of the real prediction problem and avoid leaking future or duplicate information across partitions. Representative test data makes metrics meaningful; a mechanically random split does not correct a biased or inappropriate dataset.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
