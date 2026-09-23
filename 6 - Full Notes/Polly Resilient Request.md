2026-09-22 23:34

Status: #baby

Tags: [[.NET Network Requests Sockets and Streams]]

# Polly Resilient Request

A Polly resilient request wraps a remote operation in an explicit recovery policy such as retry, fallback, or circuit breaking. The policy can inspect network exceptions and apply consistent handling to failures judged to be transient.

Retries must be bounded and appropriate to the operation. Repeating a non-idempotent request can duplicate a side effect, while retrying an invalid address or authorization failure merely adds delay and load.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
