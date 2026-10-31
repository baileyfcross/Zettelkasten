2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Message Return Address

A message return address tells a provider where to publish the response to a particular request. It is carried in message metadata because it describes transport routing rather than the business payload.

The provider no longer has to remember every requester or hard-code one reply channel. Different client types and instances can use different return destinations while sharing the same advertised request topic.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

