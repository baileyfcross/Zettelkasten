2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Autoscaling and Cost Control]]

# KEDA Event-Driven GenAI Scaling

KEDA event-driven GenAI scaling uses a ScaledObject to translate an external event or metric into an HPA-managed replica target. Queue depth, request rate, and Prometheus GPU utilization can trigger scaling even when CPU is a poor representation of pending inference work.

KEDA can scale a deployment to zero when no events exist, reducing idle cost. Polling interval, cooldown, minimum capacity, maximum replicas, authentication, and model warm-up time must be tuned together so savings do not create unacceptable first-request latency.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

