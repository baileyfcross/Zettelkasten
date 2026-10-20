2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Timeout Policy

Helidon's `@Timeout` policy places an upper bound on a managed method's execution time. The annotation supplies a nonnegative value and a time unit, with milliseconds as the default unit described by the book.

A zero value means that no timeout is configured; a negative value is an invalid fault-tolerance definition. The timeout limits how long one invocation may occupy its caller rather than deciding whether a later attempt should occur.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
