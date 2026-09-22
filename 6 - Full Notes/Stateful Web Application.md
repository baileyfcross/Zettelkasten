2026-09-21 22:12

Status: #baby

Tags: [[Cloud Scalability and Resilience Patterns]]

# Stateful Web Application

A stateful web application retains information from a user's earlier requests, such as an active session. If that state lives only in one server process, later requests may need sticky routing to the same instance, making horizontal scaling and failure recovery harder. A shared durable store can preserve session continuity across instances, but introduces its own availability and consistency requirements.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

