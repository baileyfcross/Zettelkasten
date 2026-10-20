2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Retry Policy

Helidon's `@Retry` policy repeats a method invocation after a configured failure. It can limit the number of retries and total retry duration, insert a delay, and select exception classes that trigger or abort retry behavior.

A maximum retry value of minus one means retry indefinitely, while an abort exception takes the invocation out of the retry path. The example fails the first call and succeeds on the next attempt, allowing the caller to receive a normal response after the policy repeats execution.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
