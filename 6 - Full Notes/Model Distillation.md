2026-09-05 16:28

Status: #baby

Tags: [[Speech Recognition Systems]]

# Model Distillation

Model distillation trains a smaller model to imitate the output behavior of a larger model. The larger teacher supplies informative target probabilities, allowing the compact student to retain much of its performance.

For speech recognition, distillation can make a model practical on a phone or embedded device where memory, power, and latency limit the use of a large [[Deep Neural Network]].

Amazon Bedrock applies the same teacher-student relationship to foundation models. A large teacher generates behavior that trains a smaller student to approximate its outputs, producing a model better suited to low-latency or resource-constrained use. The student trades some general capability for faster and less expensive inference on the targeted task.

# References

[[aiassistants.epub]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
