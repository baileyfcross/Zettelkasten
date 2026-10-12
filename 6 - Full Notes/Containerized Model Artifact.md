2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Deployment Architecture]]

# Containerized Model Artifact

A containerized model artifact packages inference code, runtime libraries, and optionally model weights into an immutable image. The image gives training, test, and serving environments a reproducible dependency boundary that Kubernetes can schedule and restart.

Bundling weights simplifies startup independence but creates large images and repeated network transfer. Loading versioned weights from object storage makes the image smaller but adds identity, availability, and startup dependencies, so the artifact boundary should be chosen deliberately.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

