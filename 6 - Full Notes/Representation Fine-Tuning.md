2026-09-30 17:53

Status: #baby

Tags: [[Generative AI Model Adaptation and Serving]]

# Representation Fine-Tuning

Representation fine-tuning adapts a model by learning interventions in its internal representations rather than changing the entire weight set. It treats pretrained hidden states as a rich source of semantic information that can be redirected for a downstream task.

This design can train far fewer parameters than [[Full-Parameter Fine-Tuning]], but the intervention locations and representation subspaces must be selected and evaluated carefully. Efficiency does not guarantee that the altered representation generalizes beyond its adaptation data.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
