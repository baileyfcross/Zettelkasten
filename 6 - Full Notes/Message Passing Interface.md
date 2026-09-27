2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]]

# Message Passing Interface

The Message Passing Interface is a standardized programming model for processes that exchange typed messages in a distributed-memory computation. Each process has a rank within a communicator, and the API supplies point-to-point and collective operations.

MPI specifies communication semantics rather than hiding the distributed algorithm. The program must decide how data is partitioned, which ranks communicate, and how all participants handle ordering, completion, and failure assumptions.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
