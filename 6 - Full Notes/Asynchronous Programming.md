2026-09-06 20:52

Status: #baby

Tags: [[Web Performance and Scalability]] [[.NET Task Parallelism and Asynchrony]] [[.NET Network Requests Sockets and Streams]]

# Asynchronous Programming

Asynchronous programming represents work that completes later without requiring the initiating thread to wait idly. In an ASP.NET Core data path, repository methods return tasks and controller actions await them before producing the response.

Its primary server benefit is efficient concurrency around I/O. CPU-bound work still consumes processing capacity, and converting only the outer method to async does not remove a synchronous block deeper in the call chain.

The parallel-programming source distinguishes asynchronous progress from simultaneous CPU execution. An asynchronous operation may use no worker while it waits, whereas parallel computation deliberately places independent CPU work on several workers.

# References

[[aspnetcore3andreact.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
