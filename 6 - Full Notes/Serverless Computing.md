2026-09-08 22:09

Status: #baby

Tags: [[Azure Logic Apps and Functions]]

# Serverless Computing

Serverless computing runs application functions on provider-managed infrastructure whose servers, allocation, and scaling are hidden from the developer's normal workflow. It does not mean no hardware exists; it means the application does not provision or maintain that hardware directly.

The Azure Functions model in the book scales small stateless operations according to demand and charges in relation to use. This reduces infrastructure work, while the function still needs explicit inputs, outputs, configuration, and failure handling.

The Azure discussion emphasizes allocation on demand and charging around actual execution rather than a continuously provisioned application host. That economic and operating model suits event-triggered units but still requires limits, monitoring, and external durable state.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[c8andnetcore30projectsusingazure.pdf]]
