2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Autoscaling and Cost Control]]

# KEDA Event-Driven GenAI Scaling

KEDA event-driven GenAI scaling uses a ScaledObject to translate an external event or metric into an HPA-managed replica target. Queue depth, request rate, and Prometheus GPU utilization can trigger scaling even when CPU is a poor representation of pending inference work.

KEDA can scale a deployment to zero when no events exist, reducing idle cost. Polling interval, cooldown, minimum capacity, maximum replicas, authentication, and model warm-up time must be tuned together so savings do not create unacceptable first-request latency.

The current source generalizes the control path beyond model serving: a KEDA scaler reads an external operational signal, converts it into a desired replica decision, and relies on Kubernetes scaling machinery to apply it. That makes signal semantics part of capacity policy. A noisy, late, or incorrectly aggregated metric can create oscillation or delayed recovery even when the ScaledObject itself is valid.

# References

[[kubernetesforgenerativeaisolutions.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]

