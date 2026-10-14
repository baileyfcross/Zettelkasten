2026-10-11 21:34

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Liveness Probe

A Kubernetes liveness probe asks whether a running container has entered a state from which it should be restarted. Repeated probe failure causes the kubelet to restart the container according to the pod's restart policy; it does not redirect traffic or prove that dependencies are available.

The probe should detect genuine internal deadlock or unrecoverable malfunction. Testing a fragile external dependency can turn a downstream outage into a restart storm, while thresholds that are too aggressive can repeatedly kill a slow but healthy process.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
