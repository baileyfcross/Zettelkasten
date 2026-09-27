2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]]

# MPI Point-to-Point Communication

MPI point-to-point communication transfers a message between a specific sending rank and receiving rank. Source, destination, tag, communicator, datatype, and count together identify how the receiver should match and interpret the exchange.

Blocking send and receive calls can form a deadlock if every participant waits in an incompatible order. Nonblocking operations or a deliberate protocol separates initiation from completion and permits communication to overlap computation.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
