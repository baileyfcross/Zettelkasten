2026-10-30 17:24

Status: #baby

Tags: [[Kafka Microservice Request Reply]]

# Asynchronous Request-Reply Channel

Asynchronous request-reply uses two messages—one request and one response—to reproduce a request-response interaction over one-way messaging channels. The requester publishes without a direct call stack, and a provider later sends a distinct reply message.

The pattern preserves messaging decoupling while supporting callers that still need a result. It therefore needs an advertised request destination, a return address for the reply, and correlation data that matches each response to the request that caused it.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

