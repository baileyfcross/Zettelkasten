2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Parallel Consumer Scaling

Kafka parallel consumer scaling spreads records across several partitions and assigns those partitions to different consumer instances in one group. With enough independent work, throughput can rise until partition count, consumer capacity, or downstream resources become the limit.

The book's parallel example disables requester partition pinning and uses one provider consumer per partition. This improves concurrency but gives up one global processing order because each partition advances independently.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

