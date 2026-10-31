2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Driven Adapter

A driven, or secondary, adapter reacts to work initiated through the application and connects the core to infrastructure such as a database, message broker, or third-party API. The output port belongs inside the application, while its concrete adapter belongs outside.

This dependency direction lets the core request persistence or messaging through its own abstraction. Spring can then inject a PostgreSQL, MongoDB, REST, or Kafka implementation without giving domain behavior a direct dependency on that provider.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

