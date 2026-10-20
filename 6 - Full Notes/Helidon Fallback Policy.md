2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Fallback Policy

Helidon's `@Fallback` policy redirects a failed invocation to an alternate handler. The handler can be a class implementing `FallbackHandler` or a named method in the same class with compatible arguments and a return type assignable to the protected method's return type.

Exception lists decide which failures apply the fallback and which must be skipped, with the skip list taking priority. In the example, an intentionally thrown runtime exception invokes a local method that returns a successful fallback response.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
