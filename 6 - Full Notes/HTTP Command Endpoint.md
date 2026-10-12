2026-09-22 20:53

Status: #baby

Tags: [[Application Commands and Service Boundaries]]

# HTTP Command Endpoint

An HTTP command endpoint accepts a [[Public API Contract]] and passes the represented [[Application Command]] into the application layer. The controller handles routing, deserialization, and HTTP responses; it should not contain domain rules or manipulate aggregate fields directly. HTTP is only one delivery mechanism, so keeping the endpoint thin allows the same command-handling behavior to be triggered by another interface without duplicating the [[Domain Model]].

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
