2026-09-30 17:53

Status: #baby

Tags: [[Modern Software Delivery Foundations]] · [[GenAIOps Pipeline Automation]]

# MLOps

MLOps applies DevOps principles to the development, deployment, monitoring, and maintenance of machine-learning systems. It adds data preparation, model training, experiment tracking, model packaging, validation, and performance monitoring to the ordinary code delivery lifecycle.

An MLOps pipeline may be triggered by code changes, new data, or detected model degradation. Reproducibility therefore requires versioning the code, data, model, configuration, and evaluation evidence that produced a release.

The operating record also includes the framework, checkpoint, hardware environment, and [[Model Promotion Evidence]] that justified a serving version. Orchestration, experiment tracking, pipeline execution, and inference serving are separate responsibilities that can be combined without asking one tool to own the entire lifecycle.

The current source contrasts this broad lifecycle with [[LLMOps]], which starts from many of the same deployment and monitoring practices but adds prompt templates, context windows, generated-output evaluation, LLM-specific inference optimization, and ethical controls for open-ended responses. The distinction is one of specialized operational assets and failure modes rather than a replacement for reproducible data, model, and deployment management.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[nvidiagpuinfrastructurefundamentals.pdf]]
[[masteringspringai.epub]]
