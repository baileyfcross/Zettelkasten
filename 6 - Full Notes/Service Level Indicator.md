2026-09-27 22:21

Status: #baby

Tags: [[Cloud Computing Foundations]]

# Service Level Indicator

A service level indicator is a quantitative measurement of a user-relevant aspect of service behavior, such as successful-request proportion, latency, availability, or data freshness. It turns an abstract reliability concern into an observable time series with an explicit numerator, denominator, and measurement window.

An SLI supplies the evidence used to evaluate a [[Service Level Objective]]. The indicator should reflect what users experience rather than only the health of an internal component; a running server is not a useful availability indicator if requests still fail. Consistent collection boundaries are essential because changing the measurement changes the meaning of the objective.

A request-success SLI can divide successful responses by all valid requests and normalize the result to a percentage. This makes the measured behavior explicit and separates the indicator itself from the target and time window imposed by the objective.

# References

[[clouddevopsengineersguide.pdf]]

[[observabilityintheai-nativeera.pdf]]
