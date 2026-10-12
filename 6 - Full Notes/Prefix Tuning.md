2026-09-30 17:53

Status: #baby

Tags: [[Generative AI Model Adaptation and Serving]]

# Prefix Tuning

Prefix tuning learns continuous task-specific vectors that are presented as a virtual prefix to transformer layers while the original model weights remain frozen. The learned prefix steers attention and generation without storing a complete fine-tuned model.

Because the prefix consumes representational capacity and conditions every generated result, its length and initialization affect both quality and efficiency. It is a parameter-efficient method distinct from writing a natural-language prompt.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
