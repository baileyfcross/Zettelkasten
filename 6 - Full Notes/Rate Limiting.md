2026-09-30 17:53

Status: #baby

Tags: [[Modern Software Delivery Foundations]]

# Rate Limiting

Rate limiting controls how much traffic an application or service accepts during a time interval so demand cannot exhaust its resources. Fixed-window, sliding-log, leaky-bucket, and token-bucket strategies offer different burst and fairness behavior.

Excess work may be rejected, queued, or served through a degraded path. Rate limiting is strongest when combined with caching, backpressure, [[Circuit Breaker|circuit breaking]], and capacity monitoring rather than used as the only overload defense.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
