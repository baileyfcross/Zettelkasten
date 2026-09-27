2026-09-22 23:34

Status: #baby

Tags: [[.NET Network Requests Sockets and Streams]] [[.NET Microservice Communication and Workers]]

# Polly Resilient Request

A Polly resilient request wraps a remote operation in an explicit recovery policy such as retry, fallback, or circuit breaking. The policy can inspect network exceptions and apply consistent handling to failures judged to be transient.

Retries must be bounded and appropriate to the operation. Repeating a non-idempotent request can duplicate a side effect, while retrying an invalid address or authorization failure merely adds delay and load.

Within interservice communication, Polly policies handle transient remote failures around asynchronous operations. The architecture must still decide which failures are retryable and ensure repeated execution cannot duplicate an unsafe side effect.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
