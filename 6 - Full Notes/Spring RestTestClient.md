2026-11-08 16:45

Status: #baby

Tags: [[Spring Application Testing]]

# Spring RestTestClient

Spring `RestTestClient` provides one fluent request-and-assertion API for servlet REST tests. It can bind directly to a controller for an isolated test or bind to a running server for a full HTTP exchange, then assert status, headers, decoded bodies, and JSON paths.

Using the same interaction style at both levels reduces the test rewrite needed when a controller test becomes an integration test. The binding still changes what evidence is produced: direct binding does not exercise a network socket or the complete Boot context, while server binding does. Assertions should therefore state behavior appropriate to the selected [[SpringBootTest Web Environment]].

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
