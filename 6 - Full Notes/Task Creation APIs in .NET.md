2026-09-27 00:11

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Task Creation APIs in .NET

.NET can represent new work through `Task.Run`, `Task.Factory.StartNew`, task constructors, and completed, faulted, canceled, delayed, or yielded task-producing methods. These APIs do not have identical defaults: scheduler selection, child attachment, state, and continuation behavior can differ.

The creation mechanism should match the meaning of the operation. `Task.Run` is a straightforward way to queue CPU work, while naturally asynchronous I/O should expose its existing task instead of consuming another worker merely to wait.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
