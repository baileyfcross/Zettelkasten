2026-09-06 22:42

Status: #baby

Tags: [[Data Center Storage Networking]]

# Raw Ethernet Storage Protocol

A raw Ethernet storage protocol places storage-specific messages directly in Ethernet frames instead of passing every request through a full general-purpose network stack. The shorter path can reduce processing, copies, and latency for small I/O.

The protocol must supply any required reliability, addressing, flow control, and request matching that higher layers would otherwise provide.

# References

[[bigdatamanagementandprocessing.pdf]]
