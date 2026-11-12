2026-11-11 19:33

Status: #baby

Tags: [[Microservice Testing Deployment and Scaling]]

# Quarkus Kubernetes-Native Application Build

A Quarkus Kubernetes-native application build can generate the application artifact, container image, and Kubernetes Deployment and Service manifests from one extension-aware Java project. The source combines RESTEasy Reactive, Kubernetes, and Jib extensions so a Maven build emits manifests under `target/kubernetes` while [[Jib Daemonless Java Image Build]] constructs the application image.

Quarkus targets container environments with fast startup, low memory use, live development, and both imperative and reactive programming models. The generated manifests provide defaults that can be configured before they are applied to a cluster, and a container-image extension can build and push the referenced image as part of the delivery path.

# References

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
