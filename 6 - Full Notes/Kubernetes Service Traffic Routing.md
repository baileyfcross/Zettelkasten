2026-10-30 17:24

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes Service Traffic Routing

Kubernetes Service traffic routing gives a changing set of selected pods one stable virtual endpoint. The Service selector identifies eligible pod labels, and cluster networking forwards each connection to one of those endpoints even as deployments replace or scale pods.

The Service type determines where the stable endpoint is reachable: only inside the cluster, on every node, or through a provider load balancer. Routing continuity therefore depends on selector correctness and ready endpoints rather than on fixed pod addresses.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

