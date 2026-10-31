2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Partial Reply on Timeout

Partial reply on timeout lets an aggregator return the responses collected before its waiting period expires. The release strategy is invoked with timeout context so it can emit the available records rather than discard the whole interaction.

This behavior bounds user-visible latency when one provider is slow, but completeness becomes explicit application semantics. The caller must know whether a partial set is acceptable and how missing providers are represented.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

