2026-09-27 00:11

Status: #baby

Tags: [[.NET Server Concurrency and Parallel Patterns]]

# Kestrel Threading Model

Kestrel accepts connections, performs asynchronous socket I/O, and dispatches application work without dedicating one permanently blocked thread to every connection. Its implementation evolved from a libuv-based transport toward managed sockets in later .NET Core versions.

The server's efficient I/O path does not make blocking application handlers harmless. Request code that waits synchronously can still consume thread-pool workers and reduce the number of requests that make progress concurrently.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
