2026-11-08 16:45

Status: #baby

Tags: [[Spring Messaging and Integration]]

# Spring Pulsar Subscription

Spring Pulsar connects a producer template and annotated listener to a Pulsar topic. A named subscription maintains the consumer cursor, and its mode can provide exclusive, shared, or failover consumption behavior independently of other subscriptions on the same topic.

Because Pulsar separates brokers from BookKeeper storage, it can support queuing and retained streaming with multi-tenancy, geo-replication, and tiered storage. Schema use preserves type expectations between producers and consumers, while batching improves throughput at the cost of additional latency. The subscription name is part of the delivery contract because it defines progress and sharing.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
