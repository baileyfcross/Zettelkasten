2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Microservice

A microservice is a small, independently operated process responsible for a bounded capability. The order-processing example treats autonomy as the defining property: the worker can continue running even when no new orders arrive and does not require another application process to remain alive.

Independent deployment and scaling can isolate change, but dividing one system into many services adds network, versioning, logging, and data-consistency problems. The book cautions that a microservice architecture is useful only when those costs solve a real need.

# References

[[c8andnetcore30projectsusingazure.pdf]]
