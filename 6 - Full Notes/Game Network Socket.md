2026-09-18 17:13

Status: #baby

Tags: [[Game Network Transport and Serialization]]

# Game Network Socket

A game network socket is the operating-system interface through which a game sends and receives transport data. It is created for a protocol family and transport type, then bound, connected, listened on, or addressed according to the chosen topology.

Stream sockets commonly expose [[Transmission Control Protocol]], while datagram sockets expose [[User Datagram Protocol]]. The game layer still owns message framing, serialization, validation, and integration with the update loop.

The Berkeley socket model makes those roles explicit. A UDP endpoint binds a port and uses destination addresses with send and receive operations, while a TCP server listens and accepts a separate connected socket for each client. Because any of these calls can stall, a real-time loop uses [[Non-Blocking Socket I-O]], readiness selection, or a separate networking thread.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[multiplayergameprogramming.pdf]]
