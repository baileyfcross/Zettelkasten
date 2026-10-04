2026-10-03 22:25

Status: #baby

Tags: [[Kubernetes Platform Infrastructure]]

# Kubernetes Workload and Cluster Autoscaling

Kubernetes autoscaling operates at two related levels. Horizontal and vertical workload autoscalers adjust pod replicas or resource requests, while a cluster autoscaler changes the node fleet when pending work cannot fit or capacity is no longer needed. Event-driven mechanisms can scale from application-specific signals rather than CPU or memory alone.

These loops need compatible metrics, bounds, and timing. Stabilization windows reduce flapping, scale-down policies prevent abrupt capacity loss, and cluster provisioning must be fast enough to support workload expansion. Platform design should treat workload and node scaling as one feedback system because an aggressive pod policy cannot create physical capacity by itself.

# References

[[platformengineeringforarchitects.pdf]]
