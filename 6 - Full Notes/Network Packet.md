2026-09-18 17:13

Status: #baby

Tags: [[Networked Game Programming]]

# Network Packet

A network packet is a bounded unit of data transmitted with headers that describe delivery and protocol information. Application messages may fit in one packet or be divided across several packets depending on protocol and size.

Game traffic should avoid unnecessary payload because bandwidth, serialization time, and packet frequency all contribute to network cost. A receiver must validate packet type, length, ordering information, and claimed values before applying them to game state.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
