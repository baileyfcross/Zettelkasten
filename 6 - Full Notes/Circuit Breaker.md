2026-09-30 17:53

Status: #baby

Tags: [[Modern Software Delivery Foundations]] [[Generative AI Model Adaptation and Serving]] [[Microservice Communication and Resilience]]

# Circuit Breaker

A circuit breaker stops repeated calls to a dependency that is failing, timing out, or responding too slowly. While open, it returns a predefined failure or fallback quickly so callers release resources and avoid amplifying a cascading outage.

Recovery logic later probes whether the target can resume normal traffic. The mechanism complements [[Rate Limiting]] and [[Graceful Degradation]] but addresses dependency failure rather than general request volume.

For model serving, a circuit breaker can isolate an unavailable hosted provider and immediately route an approved request class to a local or degraded fallback. The fallback must have an explicit capability and quality contract; returning a materially different model response without labeling the change hides the outage rather than handling it.

The microservices source describes the breaker as a state machine. In the closed state calls proceed while failures are counted; crossing a threshold opens the breaker so calls fail fast; after a delay, the half-open state permits limited probes to decide whether normal traffic can resume. Thresholds, wait duration, and fallback behavior must match the dependency because an over-sensitive breaker can reject healthy work and an under-sensitive one can prolong a cascade.

MicroProfile expresses that state machine through a `@CircuitBreaker` policy. A request-volume window and failure ratio determine when the circuit opens, a delay controls the transition to half-open, and a success threshold controls recovery; `skipOn` exceptions take precedence over the failure classes listed by `failOn`.

The Spring Cloud example uses Resilience4j to substitute an alternate response when a provider cannot meet its service expectation. Failing fast keeps the caller from waiting indefinitely and prevents repeated calls from worsening a dependency outage, but the fallback must be safe for the requested operation rather than merely available.

MicroProfile Fault Tolerance can place the circuit-breaker policy on a Jakarta CDI method and combine it with timeout, retry, fallback, bulkhead, or asynchronous execution. Those policies interact: retries contribute calls to the breaker's rolling volume, a fallback handles the final exhausted failure, and external configuration can tune annotation values for an environment without rebuilding the application.

The Spring Boot 4 example applies a named Resilience4j circuit breaker as a Gateway filter. A rolling request window and failure-rate threshold open the circuit, a timed open period leads to limited half-open probes, and a fallback route provides a deliberate degraded response. Actuator state makes threshold tuning and unstable dependencies observable rather than leaving fast failures unexplained.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[ultimateaiguideforlinuxengineers.pdf]]
[[artofdecodingmicroservices.epub]]

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
[[practicalmicroservicesarchitecturalpatterns.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
