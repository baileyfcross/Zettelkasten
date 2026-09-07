2026-09-06 20:52

Status: #baby

Tags: [[Web Performance and Scalability]]

# Asynchronous Programming

Asynchronous programming represents work that completes later without requiring the initiating thread to wait idly. In an ASP.NET Core data path, repository methods return tasks and controller actions await them before producing the response.

Its primary server benefit is efficient concurrency around I/O. CPU-bound work still consumes processing capacity, and converting only the outer method to async does not remove a synchronous block deeper in the call chain.

# References

[[aspnetcore3andreact.pdf]]
