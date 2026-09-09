2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Distributed System

A distributed system divides work among independently executing processes that communicate across boundaries rather than sharing one in-process state. This can support independent scaling and deployment, but failures and timing become partial: one component may succeed while another is unavailable.

The book's sales-order system separates message production, queued transport, order persistence, and confirmation. Its design gains resilience to traffic spikes while accepting more complex data integrity, logging, maintenance, and user-experience decisions.

# References

[[c8andnetcore30projectsusingazure.pdf]]
