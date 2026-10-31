2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Application Port

An application port is a consumer-agnostic entry or exit contract through which the application core communicates. In Java it can be represented by an interface, while at a broader boundary it can describe an HTTP, REST, JMS, or AMQP interaction.

The port states what the application can receive or provide without naming the concrete user interface, database, broker, or remote service. Keeping the contract with the core prevents an external delivery mechanism from becoming the business model itself.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

