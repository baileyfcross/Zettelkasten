2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Reply Partition Affinity

Kafka reply partition affinity assigns a requester instance a reply partition on which it can reliably receive its own responses. The request includes that partition identifier, and the provider copies it into the outgoing reply routing.

Sharing too few reply partitions among independent requesters can deliver a response to the wrong consumer in the group. The source therefore configures at least enough reply partitions for the requester instances whose responses must remain distinct.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

