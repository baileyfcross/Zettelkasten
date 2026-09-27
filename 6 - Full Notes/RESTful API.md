2026-09-06 20:31

Status: #baby

Tags: [[HTTP API Integration]] [[HTTP FTP SMTP and Custom Protocols]] [[REST Architectural Constraints and Hypermedia]]

# RESTful API

A RESTful API exposes resources through consistent HTTP routes and operations. The client uses request methods and resource identifiers, while the server communicates outcomes through [[HTTP Status Code|status codes]] and representations such as JSON.

This convention lets an Angular client treat a server-side controller as a data interface rather than an HTML page generator. Paging, sorting, filtering, creation, and updates can all be expressed through the same request-response boundary.

The REST constraints add more than resource-shaped routes: messages should be self-descriptive, requests stateless, responses cacheable where appropriate, and representations capable of advertising available transitions through hypermedia.

# References

[[aspnetcore3andangular9_3ed.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
