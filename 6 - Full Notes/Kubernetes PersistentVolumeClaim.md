2026-10-30 17:24

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes PersistentVolumeClaim

A Kubernetes PersistentVolumeClaim is a workload's request for persistent storage with specified capacity and access behavior. Kubernetes binds a compatible PersistentVolume to the claim, and pods refer to the claim in their volume declarations.

The claim gives the application a stable storage contract without embedding node-local paths in the pod specification. Deleting or replacing a pod therefore need not delete the database files governed by the volume's retention policy.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

