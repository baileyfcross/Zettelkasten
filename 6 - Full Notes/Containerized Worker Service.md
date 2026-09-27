2026-09-27 11:23

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Containerized Worker Service

A containerized worker service runs a .NET background processor from an immutable image without exposing an HTTP endpoint for its primary work. It typically connects outward to a queue or event broker and processes messages until the container receives a shutdown signal.

The worker must observe cancellation and externalize checkpoints or acknowledgements because a container can be replaced at any time. Independent packaging allows worker capacity to scale separately from request-serving APIs.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
