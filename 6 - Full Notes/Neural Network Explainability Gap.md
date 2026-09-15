2026-09-13 20:16

Status: #baby

Tags: [[AI Responsibility and Explainability]]

# Neural Network Explainability Gap

The neural network explainability gap arises because a trained network’s conclusion is distributed across many learned weights rather than a human-readable sequence of rules. Inspecting the computations may not yield a meaningful reason for the output.

The gap is especially important in medicine, safety, and governance, where users need grounds for trust and appeal. Evaluation must therefore include behavior on new inputs, uncertainty, monitoring, and complementary explanation methods.

Kelleher identifies three obstacles to interpreting a deep model: its scale, distributed internal representations, and successive transformations of inputs as they pass through layers. [[Neural Feature Visualization]] investigates what might trigger internal units, while a [[Neural Attribution Map]] estimates contributions to particular outputs. These views make the model more inspectable, but neither turns distributed computation into a complete human-readable reason for a decision.

# References

[[computationalthinking.epub]]

[[deeplearning_mit.epub]]
