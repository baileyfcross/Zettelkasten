2026-09-27 00:11

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Managed Foreground and Background Threads

A managed foreground thread keeps a .NET process alive until the thread finishes, while a background thread does not extend the process lifetime. When the last foreground thread ends, the runtime can terminate remaining background threads without allowing their work to complete.

The distinction is about lifetime rather than priority or computational importance. Work that must be completed or persisted should not rely on an uncoordinated background thread; its owner needs an explicit completion, cancellation, or shutdown protocol.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
