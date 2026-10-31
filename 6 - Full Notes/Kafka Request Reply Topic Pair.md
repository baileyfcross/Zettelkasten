2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Kafka Request Reply Topic Pair

A Kafka request-reply topic pair separates provider input from requester responses. Providers subscribe to the request topic, perform the operation, and publish the result to the reply topic identified by the request's headers.

The separation prevents a synchronous transport connection from defining the interaction. Topic retention, partition counts, consumer groups, reply routing, and correlation must nevertheless be configured as one protocol so a waiting requester receives the intended response.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

