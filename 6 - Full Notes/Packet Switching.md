2026-09-13 21:06

Status: #baby

Tags: [[Internet Infrastructure History]] [[Game Network Transport and Serialization]]

# Packet Switching

Packet switching divides a message into smaller addressed units that may travel independently through a network and be reassembled at the destination. Links can be shared among many conversations instead of reserved for one circuit.

The method uses network capacity flexibly and can route around unavailable paths. It differed sharply from the dedicated circuits developed for traditional telephone service.

Store-and-forward nodes receive a packet, inspect its destination, and pass it to a next hop, allowing packets from many conversations to share the same links. That sharing enables the Internet's layered service but also creates variable processing and queue delays that a real-time game experiences as [[Network Jitter]] and latency.

# References

[[computing.epub]]

[[multiplayergameprogramming.pdf]]
