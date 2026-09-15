2026-09-15 09:13

Status: #baby

Tags: [[Data Science Infrastructure and Integration]]

# Batch versus Stream Processing

Batch processing applies an operation to a dataset whose results are not urgently required. Stream processing handles each arriving element as it enters a system, making it suitable for time-sensitive labels, alerts, or measurements. The choice changes both the unit of computation and the latency the architecture must support.

The book contrasts Hadoop's batch-oriented approach with Storm's stream-oriented approach and describes Spark and Flink as combining capabilities. The general design question is not which platform name is fashionable, but whether the task needs a historical aggregate, a prompt response to each event, or both.

# References

[[datascience_mit.epub]]
