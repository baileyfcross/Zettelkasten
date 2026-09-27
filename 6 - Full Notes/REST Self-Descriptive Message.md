2026-09-27 10:58

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# REST Self-Descriptive Message

A self-descriptive message contains enough standardized metadata for a recipient to understand how to process it. The HTTP method, target URI, headers, media type, status, and body shape jointly communicate the meaning of a request or response.

Intermediaries can participate only when meaning is visible at the message boundary. Hidden session assumptions or undocumented payload conventions reduce that visibility and bind the client to knowledge outside the exchange.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
