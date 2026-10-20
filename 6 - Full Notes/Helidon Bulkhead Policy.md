2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Bulkhead Policy

Helidon's `@Bulkhead` policy caps the number of concurrent executions allowed through selected application logic. Its `value` parameter sets the positive maximum number of calls that may execute at the same time.

The policy contains overload by preventing one operation from consuming unlimited concurrent capacity. When combined with asynchronous invocation, an additional [[Helidon Bulkhead Waiting Queue]] can hold a bounded number of tasks that could not enter immediately.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
