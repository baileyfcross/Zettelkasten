2026-11-08 16:45

Status: #baby

Tags: [[Spring Security and Identity]]

# Spring Boot SSL Bundle

A Spring Boot SSL bundle gives a named, externally configured representation to key material, trust material, protocols, and related TLS settings. Servers and supported clients can refer to the same bundle instead of duplicating programmatic keystore and truststore construction.

The abstraction makes certificate configuration consistent across connectors and easier to replace per environment. It does not manage certificate issuance or rotation by itself; those files or stores still need a secure lifecycle. A server and client can use separate bundles to establish [[Mutual TLS Between Microservices]] with explicit trust in both directions.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
