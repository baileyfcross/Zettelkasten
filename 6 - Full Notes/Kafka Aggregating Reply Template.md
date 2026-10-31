2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Aggregating Reply Template

Spring Kafka's aggregating replying template collects several responses carrying the same correlation identifier and presents them as one reply result. It extends ordinary request-reply behavior with a batch of consumer records from multiple provider instances or types.

The caller can flatten, filter, deduplicate, sort, or otherwise compose those records before returning a single application response. The template is stateful while it waits, so completion count and timeout are part of its correctness.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

