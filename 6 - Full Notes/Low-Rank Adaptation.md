2026-09-29 22:24

Status: #baby

Tags: [[Generative AI Model Adaptation and Serving]]

# Low-Rank Adaptation

Low-Rank Adaptation, or LoRA, freezes the original model weights and learns smaller low-rank matrices whose product represents the task-specific weight update. This reduces the number of trainable parameters and makes domain adaptation feasible with less GPU memory than full fine-tuning.

The resulting adapter is meaningful only with its compatible base model and target layers. Choosing a rank that is too small can limit adaptation, while a larger rank increases memory and computation, so validation should compare quality against the resource savings.

LoRA represents a weight change as the product of two smaller matrices and adds that update to selected frozen layers during the forward pass. The rank controls adaptation capacity, while the scaling and target-module choices determine how strongly and where the task-specific change acts.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[kubernetesforgenerativeaisolutions.pdf]]
