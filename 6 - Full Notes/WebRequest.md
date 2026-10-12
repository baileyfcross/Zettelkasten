2026-09-22 23:34

Status: #baby

Tags: [[.NET Network Requests Sockets and Streams]]

# WebRequest

`WebRequest` is a .NET request abstraction whose concrete implementation is selected from the URI scheme. It exposes common request configuration and execution behavior while subclasses handle protocol-specific details such as HTTP, FTP, or local files.

The abstraction illustrates a pluggable request model, although the book notes that some concrete request classes were already becoming obsolete in favor of newer clients. Code should not confuse a shared interface with identical protocol semantics.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
