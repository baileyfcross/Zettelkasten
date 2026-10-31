2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Consumer Partition Concurrency

Within one Kafka consumer group, each partition is assigned to at most one consumer at a time. Maximum useful consumer concurrency is therefore bounded by the topic's partition count; additional consumers remain unassigned when every partition already has an owner.

Fewer consumers than partitions means one consumer can process several partitions. Scaling partitions and consumer instances together increases potential throughput, while preserving the single-consumer ownership that maintains per-partition order.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

