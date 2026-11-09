2026-11-08 16:45

Status: #baby

Tags: [[Spring Security and Identity]]

# Spring Security UserDetailsService

Spring Security `UserDetailsService` adapts an application's user repository to the framework's identity contract. It looks up a domain record by username, maps credential and authority fields into `UserDetails`, and leaves the security filters independent of whether the identity came from a relational database, directory, or remote service.

A reactive application implements the corresponding reactive contract and returns `Mono<UserDetails>` so lookup does not block its event loop. The adapter authenticates a stored identity; authorization still evaluates the resulting roles and authorities through request or method rules.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
