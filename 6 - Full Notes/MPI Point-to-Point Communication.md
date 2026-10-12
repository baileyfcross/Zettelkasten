2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]] [[Parallel Statistical Computing]]

# MPI Point-to-Point Communication

MPI point-to-point communication transfers a message between a specific sending rank and receiving rank. Source, destination, tag, communicator, datatype, and count together identify how the receiver should match and interpret the exchange.

Blocking send and receive calls can form a deadlock if every participant waits in an incompatible order. Nonblocking operations or a deliberate protocol separates initiation from completion and permits communication to overlap computation.

The book's statistical examples use a coordinating rank to send each worker a sample or random-stream seed, then receive a compact result such as a mean and variance. Message tags distinguish exchanges that use the same pair of ranks, while the declared datatype and count must agree at both ends.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
