2026-11-08 16:45

Status: #baby

Tags: [[Spring Messaging and Integration]]

# Spring RabbitMQ Stream

A Spring RabbitMQ stream integration writes to RabbitMQ's persistent, replicated append-only log through the stream protocol. Unlike a classic destructive queue, consumed messages remain in the stream and each consumer tracks an offset, enabling replay and large fan-out.

`RabbitStreamTemplate` is optimized for appending through the binary stream protocol, while a listener container can begin consumption from a chosen offset. The model fits retained event flows better than one-time work distribution. Retention, offset policy, and ordering semantics still need to match the application rather than being inferred from the broker type alone.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
