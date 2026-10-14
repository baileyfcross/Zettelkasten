2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Autoscaling and Cost Control]]

# Horizontal Pod Autoscaling for Model Inference

Horizontal pod autoscaling for model inference changes the number of serving replicas when a resource or custom metric moves away from its target. More replicas can increase concurrent request capacity if the cluster has enough accelerator memory and the Service distributes traffic effectively.

Replica count alone does not eliminate startup delay. Minimum capacity, scale-up policy, readiness, pending-pod monitoring, and node autoscaling must account for the time required to obtain a GPU and load model weights before the new replica contributes throughput.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

