2026-10-11 21:34

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Startup Probe

A Kubernetes startup probe protects a slow-starting container from liveness enforcement until initialization succeeds. During this period Kubernetes evaluates the startup probe instead of interpreting ordinary liveness failures as evidence that the process must be restarted.

Its failure threshold and interval should cover the credible worst-case startup time without hiding a permanently broken launch. After success, liveness and readiness resume their separate responsibilities for restart decisions and traffic eligibility.

This separation is especially useful for Jakarta EE processes whose boot sequence must discover beans, create resources, establish connections, or initialize an application server. The startup budget should reflect measured cold-start behavior; increasing it indefinitely only delays detection of a launch that will never become healthy.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
