2026-09-13 21:06

Status: #baby

Tags: [[Internet Infrastructure History]] [[TCP UDP and Internet Protocol Addressing]]

# Transmission Control Protocol

Transmission Control Protocol provides a reliable ordered data stream over an unreliable packet network. It divides application data, tracks delivery, retransmits missing pieces, and reassembles the original sequence.

TCP operates end to end between hosts rather than requiring every network link to guarantee delivery. Applications can use its service without managing each packet directly.

This reliability can add delay when a missing segment blocks later data until retransmission succeeds. Games therefore use TCP for information that must arrive intact, while rapidly changing real-time updates often favor [[User Datagram Protocol]].

# References

[[computing.epub]]
[[gameprogrammingalgorithmsandtechniques.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
