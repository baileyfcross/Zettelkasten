2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]] [[.NET Network Requests Sockets and Streams]]

# C# Async and Await

An `async` method can use `await` to pause its logical execution until an awaitable operation completes. The method returns control to its caller instead of blocking the current thread and later resumes from the suspended point.

Asynchronous code improves responsiveness and scalability for waiting-heavy operations, but it does not make CPU work inherently faster. Tasks should normally be awaited, exceptions must be observed, and cancellation should be propagated through the operation graph.

The conference-counter example uses waiting customers to motivate nonblocking work. In an application, `await` yields while an asynchronous operation is incomplete instead of occupying a thread solely to wait; many requests can therefore make progress with fewer blocked workers.

An asynchronous method should normally return `Task` or `Task<T>` rather than `void`, and the async chain should continue to a caller that can observe completion. Context capture is useful for thread-affine interfaces but can be disabled in reusable code that has no such dependency.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
