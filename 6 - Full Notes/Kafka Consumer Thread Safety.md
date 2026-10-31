2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Consumer Thread Safety

A Kafka producer can be shared across threads, but a Kafka consumer is not thread-safe. The default consumer processes its assigned records on one thread and must not be invoked concurrently from unrelated processing threads.

Parallelism normally comes from additional consumers and partitions rather than sharing one consumer instance. A more advanced design can decouple polling and acknowledgment from time-consuming work, but that requires explicit ordering and completion control beyond a simple listener.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

