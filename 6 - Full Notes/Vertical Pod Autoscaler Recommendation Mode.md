2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Autoscaling and Cost Control]]

# Vertical Pod Autoscaler Recommendation Mode

Vertical Pod Autoscaler recommendation mode observes pod CPU and memory use and proposes better requests without automatically changing running workloads. It provides evidence for right-sizing while avoiding evictions or a moving resource baseline.

Recommendation mode is especially useful for GenAI support services whose requests were guessed initially. GPU extended resources are governed separately, and observed peaks, initialization behavior, and service objectives should be considered before applying a recommendation mechanically.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

