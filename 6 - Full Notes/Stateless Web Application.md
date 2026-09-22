2026-09-21 22:12

Status: #baby

Tags: [[Cloud Scalability and Resilience Patterns]]

# Stateless Web Application

A stateless web application does not require the server handling a request to retain session information for the next request. Any healthy instance can process a later call when the needed context accompanies the request or resides in an appropriate shared service. This permits more even load balancing and simpler recovery after an instance fails, though the wider system may still contain durable state elsewhere.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

