2026-11-08 16:45

Status: #baby

Tags: [[Spring Messaging and Integration]]

# Spring JmsClient

Spring `JmsClient` is a fluent interface for sending content to a Java Message Service destination. A call selects a queue or topic, supplies the payload, and relies on the configured message converter to produce an interoperable format such as JSON.

JMS preserves a common API across compliant brokers and supports queue, publish-subscribe, selectors, and transaction-oriented enterprise workflows. Listener containers behind `@JmsListener` manage connections, delivery, acknowledgement, and payload conversion for consumers. Connection pooling is important because repeatedly constructing broker connections is expensive.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
