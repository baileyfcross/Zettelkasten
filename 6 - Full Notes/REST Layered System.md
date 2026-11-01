2026-09-27 10:58

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# REST Layered System

The layered-system constraint permits intermediaries such as gateways, proxies, and caches to sit between a REST client and the origin service. A participant interacts with the adjacent layer without requiring knowledge of the complete path.

Layers can provide caching, security, routing, or load distribution. Their participation depends on self-descriptive messages and must preserve the externally visible semantics expected by the client.

The book emphasizes that each layer communicates through a defined interface and can be extended or scaled for its own responsibility. This modularity enables a storage, routing, or presentation layer to change without requiring every other layer to share its implementation details.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[masteringrestapis.epub]]
