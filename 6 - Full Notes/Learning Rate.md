2026-09-15 02:20

Status: #baby

Tags: [[Neural Network Training]]

# Learning Rate

The learning rate scales how far a training rule changes model weights in response to an error or gradient. With [[Gradient Descent]], a large rate takes bigger steps through [[Model Weight Space|weight space]]; a small rate takes smaller ones.

Kelleher explains the tradeoff using a ball rolling toward a hole: steps that are too large may pass a useful minimum or make training unstable, while very small steps can make progress slow. The rate is a [[Hyperparameter]] chosen for the training process, not a connection weight learned by the ordinary weight-update rule. Some schedules start larger and reduce it as training progresses.

# References

[[deeplearning_mit.epub]]
