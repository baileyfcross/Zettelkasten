2026-10-11 21:34

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]] [[Microservice Testing Deployment and Scaling]]

# Kubernetes Readiness Probe

A Kubernetes readiness probe asks whether a pod should currently receive traffic. When it fails, the pod can remain running while its address is removed from matching Service endpoints, allowing startup, overload, or temporary dependency problems to be isolated without forcing a restart.

Readiness should represent the work the service promises to accept. A shallow process check can route traffic before initialization is complete, while a probe coupled to every optional dependency can unnecessarily remove otherwise useful capacity.

The microservices source uses readiness to protect deployments and scaling events. A new replica should not join the Service's traffic set until initialization and required connections are complete, and a temporarily overloaded instance can withdraw without being restarted. Readiness thus gives the routing layer evidence about current service capacity while liveness answers a separate recovery question.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
[[artofdecodingmicroservices.epub]]
