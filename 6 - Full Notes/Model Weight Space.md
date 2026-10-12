2026-09-15 02:18

Status: #baby

Tags: [[Machine Learning Foundations]]

# Model Weight Space

Weight space is the set of possible parameter combinations for a model. If a model has two trainable weights, each point in a two-axis weight space specifies one candidate weighted mapping. Moving in this space changes the model, not the input examples in [[Model Input Space]].

Training searches for a point whose model fits the examples well. An [[Loss Function|error or loss function]] can assign a score to each point, creating an error surface over weight space; [[Gradient Descent]] uses local changes in that score to guide parameter updates. Kelleher uses this geometric view to connect a simple linear model to neural-network training.

In a fitted linear model, the magnitude and sign of a weight describe how an attribute contributes under the model: a negative mileage weight lowers the estimated price as mileage rises, while a weight near zero suggests little contribution. These interpretations belong to the selected model and data rather than proving a universal causal effect.

# References

[[deeplearning_mit.epub]]

[[machinelearning_mit.epub]]
