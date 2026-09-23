2026-09-22 23:34

Status: #baby

Tags: [[.NET Network Requests Sockets and Streams]]

# StreamReader and StreamWriter

`StreamReader` and `StreamWriter` wrap a .NET stream with text-oriented reading and writing. They translate between characters and bytes using an encoding and offer operations such as line-based reads and writes.

When used over a `NetworkStream`, both endpoints must agree on encoding and framing. Flushing and disposal affect when buffered text is transmitted and whether the underlying stream remains usable.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
