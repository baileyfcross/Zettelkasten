2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Key-Based Partition Ordering

Kafka's default producer partitioning sends records with the same non-null key to the same topic partition. Because Kafka preserves record order within a partition, a stable business key such as a customer or account identifier can preserve that key's processing order.

A null key allows partition selection without that affinity. The ordering guarantee comes from co-location in one partition, not from the key as an abstract property, so changing the routing strategy can change the effective ordering boundary.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

