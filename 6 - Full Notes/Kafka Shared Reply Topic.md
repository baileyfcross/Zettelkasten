2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Shared Reply Topic

A shared Kafka reply topic carries responses for more than one replying template or requester. Correlation identifiers and consumer routing distinguish the replies instead of assigning every requester a physically separate topic.

Spring Kafka can mark the reply topic as shared so a response not expected by one template is treated as normal shared-topic behavior rather than a transport error. Sharing saves destinations but makes correct correlation and partition ownership essential.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

