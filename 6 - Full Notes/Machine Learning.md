2026-09-05 16:28

Status: #baby

Tags: [[Machine Learning and Neural Networks]] · [[Data Ethics and Digital Power]] · [[ML.NET Recommendation Applications]]

# Machine Learning

Machine learning develops models by finding patterns in data rather than requiring a programmer to specify every decision rule. The learned model can then predict a label, representation, or action for new inputs.

The main training setups include [[Supervised Learning]], [[Unsupervised Learning]], and [[Reinforcement Learning]]. Their difference lies in the feedback available during learning: labels, latent structure, or rewards from interaction.

Training from examples changes adjustable model parameters instead of requiring a programmer to specify every decision rule. In a neural network, [[Forward Propagation]] produces an output, a [[Loss Function]] measures its difference from the desired result, and [[Backpropagation]] supplies information for changing weights and biases. Performance on a [[Test Dataset]] then checks whether the fitted behavior transfers to unseen examples.

A learned pattern is not automatically a causal explanation or a fair basis for action. Model behavior depends on the [[Data Science Pipeline]], including how examples were captured, selected, represented, and interpreted. Ethical evaluation therefore examines the data and institutional use as well as predictive performance.

The emotion-detector chapter contrasts training a custom model with consuming a provider's pretrained service. A hosted model reduces the expertise and time needed by the application developer, but the application then depends on the provider's training data and the questions its service can answer.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aiassistants.epub]]

[[aiethics.epub]]

[[algorithms.epub]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
