2026-09-30 17:53

Status: #baby

Tags: [[Modern Software Delivery Foundations]] [[Microservice Security and Observability]]

# Rate Limiting

Rate limiting controls how much traffic an application or service accepts during a time interval so demand cannot exhaust its resources. Fixed-window, sliding-log, leaky-bucket, and token-bucket strategies offer different burst and fairness behavior.

Excess work may be rejected, queued, or served through a degraded path. Rate limiting is strongest when combined with caching, backpressure, [[Circuit Breaker|circuit breaking]], and capacity monitoring rather than used as the only overload defense.

At a microservice gateway, rate limiting can apply a shared traffic policy before requests consume downstream capacity. A distributed counter store can coordinate limits across gateway instances, but the limit's identity, time window, burst behavior, and failure mode must be explicit. A policy that rejects traffic should return a predictable response and produce metrics so operators can distinguish abusive demand from an undersized service.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
[[artofdecodingmicroservices.epub]]
