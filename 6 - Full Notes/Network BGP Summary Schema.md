2026-09-27 22:03

Status: #baby

Tags: [[AI-Assisted Network Output Parsing]]

# Network BGP Summary Schema

A network BGP summary schema represents a router’s local identity and its peer states in a structure that conventional code can inspect. Useful fields include router ID, local autonomous system, total and established peer counts, and a neighbor list containing address, remote AS, state, uptime, and received-prefix count.

The structure supports deterministic checks after extraction. Code can compare established peers with total peers, enumerate any neighbor not in `Established`, and flag a zero-prefix session without asking the model to make that exact decision. The schema therefore separates flexible text normalization from repeatable health logic.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
