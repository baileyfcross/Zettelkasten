2026-09-30 17:53

Status: #baby

Tags: [[Modern Software Delivery Foundations]] [[Generative AI Model Adaptation and Serving]]

# Circuit Breaker

A circuit breaker stops repeated calls to a dependency that is failing, timing out, or responding too slowly. While open, it returns a predefined failure or fallback quickly so callers release resources and avoid amplifying a cascading outage.

Recovery logic later probes whether the target can resume normal traffic. The mechanism complements [[Rate Limiting]] and [[Graceful Degradation]] but addresses dependency failure rather than general request volume.

For model serving, a circuit breaker can isolate an unavailable hosted provider and immediately route an approved request class to a local or degraded fallback. The fallback must have an explicit capability and quality contract; returning a materially different model response without labeling the change hides the outage rather than handling it.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[ultimateaiguideforlinuxengineers.pdf]]
