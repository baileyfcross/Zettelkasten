2026-11-08 16:45

Status: #baby

Tags: [[Spring Messaging and Integration]]

# Spring RSocket Interaction Models

Spring RSocket supports four message interactions over a persistent, multiplexed Reactive Streams connection: request-response, fire-and-forget, request-stream, and bidirectional channel. A message-mapped handler binds a route to application logic, while an RSocket requester invokes the route from a client.

The protocol is message-centric and carries backpressure, allowing a slow consumer to control the rate of a returned stream. TCP suits internal communication, while WebSocket transport can traverse browser and firewall boundaries. Connection retry and resume behavior must be configured deliberately because a persistent connection can still fail.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
