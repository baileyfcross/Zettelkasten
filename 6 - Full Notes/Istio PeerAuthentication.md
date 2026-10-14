2026-09-29 22:09

Status: #baby

Tags: [[Istio Service Mesh Operations]]

# Istio PeerAuthentication

Istio PeerAuthentication controls how workloads accept mutual TLS connections from other mesh workloads. Strict mode requires authenticated mesh identity, permissive mode supports migration alongside plaintext clients, and workload or port scoping can refine the policy.

Mutual TLS proves the peer workload identity and protects traffic in transit; it does not by itself decide whether that identity may call the service. [[Istio Authorization Policy]] uses the authenticated principal and request context to make that separate decision.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

