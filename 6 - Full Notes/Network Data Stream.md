2026-09-22 23:34

Status: #baby

Tags: [[.NET Network Requests Sockets and Streams]]

# Network Data Stream

A network data stream presents the packets received for a connection as a sequential source of bytes. Application code reads the sequence as data becomes available rather than handling every transport packet as an independent business message.

Stream delivery does not define message boundaries. A protocol must use a length, delimiter, terminal value, or other framing rule so the reader knows when one logical value is complete.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
