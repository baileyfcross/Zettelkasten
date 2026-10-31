2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Explicit Partition Routing

Kafka permits a producer to name a partition explicitly when constructing a record. An explicit partition overrides the normal key-based choice, although the key is still stored with the record.

This allows a requester to pin messages to a known processing or reply path, but it also places partition-count and load-distribution knowledge in the producer. Explicit routing should therefore be part of the inter-service protocol rather than an accidental local choice.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

