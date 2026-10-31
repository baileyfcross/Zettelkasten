2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Reply Listener Container

A Kafka reply listener container subscribes to the topic or partitions on which request responses arrive. The replying template uses records delivered by this container to complete the matching pending request.

Its consumer factory defines reply deserialization, while container properties define destinations and acknowledgment behavior. The container is therefore part of the request-reply mechanism, not merely a background listener unrelated to the requester.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

