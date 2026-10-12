2026-09-22 23:34

Status: #baby

Tags: [[OSI Layers Packets and Network Streams]]

# Protocol Data Unit

A protocol data unit is the data passed through a layer of the network stack together with the headers or footers that give that layer's peer enough context to interpret it. Encapsulation adds this context as data moves downward through a sender's stack.

The receiving host removes and interprets the corresponding layer information as the data moves upward. The exact name and fields vary by layer and protocol, but the purpose is to preserve the information required for standardized peer communication.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
