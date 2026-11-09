2026-11-08 16:45

Status: #baby

Tags: [[Spring Messaging and Integration]]

# Spring WebSocket STOMP Broker

Spring WebSocket support can layer STOMP destinations and frames over a persistent full-duplex [[WebSocket API Connection]]. An endpoint performs the initial handshake, a broker prefix identifies destinations clients may subscribe to, and `SimpMessagingTemplate` lets server-side components publish updates to those subscribers.

The in-memory simple broker is suitable for one application instance, but a multi-instance deployment needs an external broker or another distribution mechanism so clients connected to different nodes receive the same event. Secure WebSocket transport, endpoint authorization, heartbeat policy, and reconnection remain part of the long-lived channel design.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
