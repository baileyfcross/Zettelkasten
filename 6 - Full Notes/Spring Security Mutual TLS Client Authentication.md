2026-11-08 16:45

Status: #baby

Tags: [[Spring Security and Identity]]

# Spring Security Mutual TLS Client Authentication

Spring Security can use a mutually authenticated TLS certificate as the client's authentication method. A server truststore validates the presented certificate, and an authorization server can bind a registered OAuth client to certificate identity instead of accepting a reusable client secret.

In the book's service flow, TLS protects the connection, the client certificate proves the calling workload, and a scoped [[JSON Web Token]] authorizes the requested operation. These controls answer different questions and should not be collapsed into one. [[Spring Boot SSL Bundle]] supplies the key and trust configuration, while production certificate issuance and rotation belong to managed PKI automation.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
