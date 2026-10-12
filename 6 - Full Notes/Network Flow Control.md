2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]]

# Network Flow Control

Network flow control prevents a sender or upstream link from delivering data faster than the receiver and intermediate buffers can absorb it. Credits, windows, or backpressure communicate available capacity through the path.

Without flow control, overload produces buffer exhaustion and loss; overly conservative control leaves links idle. In distributed computation, these effects influence whether communication overlaps useful work or stalls the participating processes.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
