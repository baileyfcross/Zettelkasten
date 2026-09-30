2026-09-29 22:09

Status: #baby

Tags: [[Istio Service Mesh Operations]]

# Istio DestinationRule

An Istio DestinationRule defines policies applied after routing chooses a service destination. It can name subsets by workload labels and configure load balancing, connection pools, outlier detection, and TLS for traffic sent to that host.

VirtualService traffic splits commonly refer to these subsets for canary or blue-green delivery. A subset without matching endpoints, or TLS settings that disagree with the destination, can turn a syntactically valid rollout into failed requests.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

