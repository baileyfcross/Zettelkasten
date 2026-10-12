2026-10-11 21:34

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Startup Probe

A Kubernetes startup probe protects a slow-starting container from liveness enforcement until initialization succeeds. During this period Kubernetes evaluates the startup probe instead of interpreting ordinary liveness failures as evidence that the process must be restarted.

Its failure threshold and interval should cover the credible worst-case startup time without hiding a permanently broken launch. After success, liveness and readiness resume their separate responsibilities for restart decisions and traffic eligibility.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
