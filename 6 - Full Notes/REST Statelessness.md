2026-09-27 10:58

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# REST Statelessness

REST statelessness requires each request to carry the information needed for the server to understand and authorize that interaction. The server does not depend on conversational state retained from an earlier request by the same client.

Resource state can still be stored persistently, and clients can still maintain application state. Removing hidden per-client conversation state makes requests easier to distribute among service instances, while tokens or other request data must be sent again when needed.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
