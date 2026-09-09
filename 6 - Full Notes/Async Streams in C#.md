2026-09-08 21:16

Status: #baby

Tags: [[.NET Files Streams and Serialization]], [[.NET Task Parallelism and Asynchrony]]

# Async Streams in C#

C# 8 introduced asynchronous streams so a sequence can produce values over time without blocking while each value becomes available. A producer returns `IAsyncEnumerable<T>`, and a consumer processes it with `await foreach`.

This model combines the incremental nature of enumeration with asynchronous waiting, making it suitable for paged services, streamed data, and other sources that do not complete all at once. Cancellation and disposal remain important because enumeration may hold resources across multiple awaits.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
