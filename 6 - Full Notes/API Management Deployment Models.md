2026-11-08 16:00

Status: #baby

Tags: [[REST API Performance Scaling and Observability]]

# API Management Deployment Models

An API management service can apply its capabilities through a proxy, server agents, or a hybrid deployment. A proxy places the management gateway in the request path so all traffic passes through its policy boundary; an agent is installed with the server and can apply selected features without intercepting traffic through a separate gateway.

A hybrid model chooses capabilities from both arrangements. The deployment choice affects latency, failure domains, coverage, operational ownership, and how uniformly security, analytics, caching, and traffic policies are enforced. It should therefore be selected as an architecture decision rather than treated as a transparent installation detail.

# References

[[prorestfulapiswithmicronaut.epub]]
