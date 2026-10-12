2026-09-29 22:24

Status: #baby

Tags: [[Generative AI Model Adaptation and Serving]]

# Prompt Tuning

Prompt tuning learns a small set of soft prompt tokens from labeled domain data while leaving the main model parameters unchanged. The learned tokens steer model behavior for a task with substantially less training and storage than full fine-tuning.

Soft prompt tokens are model parameters, not ordinary written instructions. They must be versioned with the base model and evaluated on representative inputs, because a compact adaptation can still overfit a dataset or fail outside its training distribution.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

