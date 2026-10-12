2026-09-27 11:11

Status: #baby

Tags: [[.NET Microservice Communication and Workers]]

# Hosted Service Lifecycle

The hosted service lifecycle connects background work to application startup and shutdown. The host starts registered services after composition, signals cancellation when the process is stopping, and gives asynchronous work a limited opportunity to finish cleanly.

Lifecycle-aware code stops accepting new work, completes or safely abandons current work, and releases broker connections and other resources. Ignoring shutdown signals can leave partially processed messages or delay container termination.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
