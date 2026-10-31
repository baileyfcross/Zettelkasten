2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Driving Adapter

A driving, or primary, adapter initiates an action against the application core. Browser controllers, command handlers, automated tests, batch scripts, and message listeners can all drive the same use case through an input port.

Both the input contract and its use-case implementation remain inside the application boundary. The adapter translates its external protocol into that contract, allowing another entry mechanism to be added without duplicating the business operation.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

