2026-09-30 17:53

Status: #baby

Tags: [[Modern Software Delivery Foundations]]

# Circuit Breaker

A circuit breaker stops repeated calls to a dependency that is failing, timing out, or responding too slowly. While open, it returns a predefined failure or fallback quickly so callers release resources and avoid amplifying a cascading outage.

Recovery logic later probes whether the target can resume normal traffic. The mechanism complements [[Rate Limiting]] and [[Graceful Degradation]] but addresses dependency failure rather than general request volume.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
