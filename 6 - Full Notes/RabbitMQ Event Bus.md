2026-09-27 11:11

Status: #baby

Tags: [[.NET Microservice Communication and Workers]]

# RabbitMQ Event Bus

A RabbitMQ event bus carries integration events from producing services to independently running consumers through exchanges and queues. The producer publishes a message without needing a direct HTTP connection to every service that reacts to it.

This communication model improves temporal and deployment decoupling, but it introduces delivery concerns. Consumers need explicit acknowledgement, retry, idempotency, and failure-handling rules because a message can arrive more than once or outlive the process that first receives it.

The Spring AMQP example makes the routing topology explicit: a producer publishes to a topic exchange, bindings route matching keys to queues, and listener containers acknowledge consumption. RabbitMQ streams add a retained append-only option whose consumers track offsets rather than deleting messages, so one broker can support both work distribution and replayable event feeds with different semantics.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
