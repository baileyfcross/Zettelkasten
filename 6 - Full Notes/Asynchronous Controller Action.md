2026-09-06 20:52

Status: #baby

Tags: [[Web Performance and Scalability]] [[ASP.NET Core Page and MVC Development]]

# Asynchronous Controller Action

An asynchronous controller action returns a task and awaits asynchronous repository or service operations. While an external operation is incomplete, the request does not need to occupy a thread that can perform no useful work.

This can improve server scalability under concurrent I/O-bound requests, but it does not make the underlying database operation intrinsically faster. The asynchronous path should extend through the dependencies rather than blocking inside them.

# References

[[aspnetcore3andreact.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
