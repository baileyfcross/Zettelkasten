2026-11-08 16:45

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]]

# Serializable Transaction Retry

Serializable transaction retry repeats an entire transaction after the database aborts it to preserve an execution equivalent to some serial order. In a distributed SQL system, two transactions may read overlapping state and make decisions that cannot both commit without violating that guarantee, so one receives a retryable serialization failure.

The retry boundary must include every read and write that informed the decision, and the work should be safe to execute again. Backoff and a maximum attempt count limit contention amplification. Exhausted work needs an explicit client response or durable queue, while metrics reveal when retries are masking a schema or workload hotspot.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
