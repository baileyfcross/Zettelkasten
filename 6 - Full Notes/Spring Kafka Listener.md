2026-11-08 16:45

Status: #baby

Tags: [[Spring Messaging and Integration]]

# Spring Kafka Listener

Spring Kafka's `@KafkaListener` registers a method as a consumer of one or more Kafka topics. Its consumer group determines which instances share partition work, and receiving a `ConsumerRecord` exposes metadata such as the key, partition, and offset beside the payload.

A stable key can preserve per-entity ordering by routing related records to the same partition. Consumer-group concurrency cannot create more useful parallelism than the available partitions, and processing must account for replay and duplicate delivery. Tests need an asynchronous completion signal rather than asserting immediately after a producer sends a record.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
