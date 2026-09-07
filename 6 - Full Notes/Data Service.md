2026-09-06 20:37

Status: #baby

Tags: [[Front-End Service Design]]

# Data Service

A data service centralizes client operations that exchange data with a back-end API. Instead of letting several components call [[Angular HttpClient]] directly, it provides named methods for getting, creating, and updating application records.

The layer creates one place for URL construction, response typing, post-processing, error handling, and retries. Domain-specific services can extend a typed base service while components depend on their narrower interfaces.

# References

[[aspnetcore3andangular9_3ed.pdf]]
