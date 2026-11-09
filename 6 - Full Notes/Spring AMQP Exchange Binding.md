2026-11-08 16:45

Status: #baby

Tags: [[Spring Messaging and Integration]]

# Spring AMQP Exchange Binding

Spring AMQP can declare a RabbitMQ exchange, queue, and binding as managed beans so the broker topology exists when the application starts. A producer publishes to the exchange with a routing key, and the binding rule determines which queue receives the message.

A topic binding such as `customer.#` routes a family of customer events without making the producer name a consumer queue. This preserves the exchange-based model behind [[RabbitMQ Event Bus]] and lets new queues subscribe independently. A production design still needs durable declarations, acknowledgements, dead-letter handling, prefetch, and idempotent consumers.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
