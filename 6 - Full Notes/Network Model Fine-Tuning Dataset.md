2026-09-27 18:30

Status: #baby

Tags: [[AI-Assisted Network Automation]]

# Network Model Fine-Tuning Dataset

A network model fine-tuning dataset contains curated examples of requests and desired responses in the provider's required training format. It can teach recurring Cisco-style configuration patterns, local terminology, or output conventions more persistently than repeating the same examples in every prompt.

Dataset quality sets the ceiling on the specialization. Addresses and secrets should be sanitized, examples should cover important variants, and answers must embody the standard the model is expected to reproduce. Training examples must be separated from held-out cases used for [[Fine-Tuned Network Model Verification]].

# References

[[ainetworkingcookbook.pdf]]
