2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]]

# Switching Strategies

A switching strategy determines how a communication network allocates intermediate links and buffers while moving a message. Circuit switching reserves a path, whereas packet-oriented strategies divide traffic and share links over time.

The choice changes setup latency, buffer pressure, throughput, and behavior under contention. Parallel programs experience these properties as communication delay even when their message-passing API presents the same logical send and receive operations.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
