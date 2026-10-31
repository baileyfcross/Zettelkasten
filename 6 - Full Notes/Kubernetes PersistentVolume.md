2026-10-30 17:24

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes PersistentVolume

A Kubernetes PersistentVolume is a cluster storage resource whose lifecycle is separated from any one pod. It represents storage provisioned by an administrator or storage system and exposes capacity and access characteristics that workloads can claim.

Pods do not normally name a volume implementation directly. They mount storage through a claim, allowing a replacement pod to reconnect to data that outlives the container and pod instances that used it.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

