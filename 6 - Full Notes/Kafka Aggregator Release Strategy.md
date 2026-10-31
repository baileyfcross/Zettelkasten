2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Aggregator Release Strategy

A Kafka aggregator release strategy decides when the collected replies are sufficient to emit a result. The source's strategy releases when the expected provider count has responded or when the configured timeout is reached.

Production criteria may be dynamic because provider availability and minimum acceptable coverage can vary by request. The strategy must distinguish a complete result from a timeout and define whether late or excess replies are ignored, retained, or treated as errors.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

