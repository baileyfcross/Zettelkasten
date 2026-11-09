2026-11-08 16:45

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring Cloud Stream Functional Binding

Spring Cloud Stream binds Java `Supplier`, `Function`, and `Consumer` beans to logical message destinations. A binder translates those logical bindings to RabbitMQ, Kafka, or another supported broker, allowing the business function to remain independent of a broker-specific client API.

External configuration maps a function name to its input or output destination, content type, and consumer group. A named group gives consumers a durable, load-balanced subscription so messages can wait while the application is offline. Broker portability does not erase delivery differences, so schemas, dead-letter handling, retries, ordering, and idempotency remain explicit.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
