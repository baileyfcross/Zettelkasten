2026-09-29 22:24

Status: #baby

Tags: [[Generative AI Model Adaptation and Serving]]

# Low-Rank Adaptation

Low-Rank Adaptation, or LoRA, freezes the original model weights and learns smaller low-rank matrices whose product represents the task-specific weight update. This reduces the number of trainable parameters and makes domain adaptation feasible with less GPU memory than full fine-tuning.

The resulting adapter is meaningful only with its compatible base model and target layers. Choosing a rank that is too small can limit adaptation, while a larger rank increases memory and computation, so validation should compare quality against the resource savings.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

