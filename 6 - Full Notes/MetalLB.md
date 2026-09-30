2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# MetalLB

MetalLB provides external IP addresses for LoadBalancer Services in clusters that do not have a cloud-provider load-balancer implementation. Address pools declare usable ranges, while its controllers and speakers advertise or respond for assigned addresses using the configured Layer 2 or routing behavior.

Address allocation must agree with the surrounding network. Pools can be scoped, automatic assignment can be disabled, and a service can request a specific address, but duplicate ownership or an unroutable range will leave a correct Kubernetes object unreachable.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

