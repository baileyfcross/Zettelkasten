2026-09-18 17:13

Status: #baby

Tags: [[Networked Game Programming]]

# Game Network Socket

A game network socket is the operating-system interface through which a game sends and receives transport data. It is created for a protocol family and transport type, then bound, connected, listened on, or addressed according to the chosen topology.

Stream sockets commonly expose [[Transmission Control Protocol]], while datagram sockets expose [[User Datagram Protocol]]. The game layer still owns message framing, serialization, validation, and integration with the update loop.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
