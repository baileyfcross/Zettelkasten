2026-09-15 02:18

Status: #baby

Tags: [[Machine Learning Foundations]]

# Inductive Bias in Machine Learning

Inductive bias is the set of assumptions a learning algorithm uses to prefer some functions over others beyond what the examples alone establish. A model restricted to straight-line relationships, for instance, assumes linear structure even when the dataset might also support more complex mappings.

The bias counterbalances the [[Ill-Posed Learning Problem|ambiguity of learning from limited examples]]. If it is too restrictive for the domain, the chosen function may [[Model Underfitting|underfit]]; if it is too permissive relative to the available data, it may [[Model Overfitting|overfit]] noise. Kelleher describes neural networks as having relatively weak bias, which helps them learn flexible relationships but also increases their demand for substantial data.

One common bias assumes that similar inputs have similar outputs and that real processes change smoothly except at meaningful boundaries. Another favors a simple explanation over a needlessly elaborate one. Neither is universally correct; each narrows the set of models consistent with the observations so a learner can generalize beyond them.

# References

[[deeplearning_mit.epub]]

[[machinelearning_mit.epub]]
