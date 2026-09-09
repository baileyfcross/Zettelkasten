2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Waiting for .NET Tasks

.NET can wait for one task, any task in a set, or every task in a set. Synchronous APIs such as `Wait`, `WaitAny`, and `WaitAll` block the calling thread, whereas asynchronous waiting allows the caller to yield until completion.

The wait shape should match the dependency: continue after the first useful result, after all required results, or after one specific operation. Blocking is especially risky in responsive and server applications because it consumes a thread and may participate in a deadlock.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
