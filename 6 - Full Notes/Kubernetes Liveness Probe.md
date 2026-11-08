2026-10-11 21:34

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]] [[Microservice Testing Deployment and Scaling]]

# Kubernetes Liveness Probe

A Kubernetes liveness probe asks whether a running container has entered a state from which it should be restarted. Repeated probe failure causes the kubelet to restart the container according to the pod's restart policy; it does not redirect traffic or prove that dependencies are available.

The probe should detect genuine internal deadlock or unrecoverable malfunction. Testing a fragile external dependency can turn a downstream outage into a restart storm, while thresholds that are too aggressive can repeatedly kill a slow but healthy process.

For a microservice, liveness is a recovery signal rather than a traffic signal. It should answer whether restarting this container can restore useful execution. A service can be live while temporarily unready, so using the same broad dependency check for both liveness and readiness can convert an external outage into needless replacement of healthy processes.

Jakarta EE startup can involve dependency injection, resource initialization, and connection establishment, so the liveness check needs enough initial delay or startup-probe protection to avoid classifying initialization as failure. Once active, it should report an internal condition a restart can repair rather than aggregate every optional dependency.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
[[artofdecodingmicroservices.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
