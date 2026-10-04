2026-10-03 22:25

Status: #baby

Tags: [[Platform Architecture and Capability Design]]

# Centralized Platform Capability

A centralized platform capability runs as a shared service for many teams, environments, or regions. One instance is generally easier to patch, secure, observe, and govern, and it can concentrate specialist knowledge behind a consistent interface.

Centralization also enlarges failure scope and can create capacity bottlenecks or a noisy-neighbor problem. The service may require privileged access to every target environment, increasing its dependency and trust surface. A central capability is appropriate when management simplicity and shared consistency outweigh isolation, latency, and regional constraints.

# References

[[platformengineeringforarchitects.pdf]]
