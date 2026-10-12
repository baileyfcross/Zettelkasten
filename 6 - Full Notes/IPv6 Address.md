2026-09-18 17:13

Status: #baby

Tags: [[Game Network Transport and Serialization]] [[TCP UDP and Internet Protocol Addressing]]

# IPv6 Address

An IPv6 address is a 128-bit Internet Protocol address, conventionally written as hexadecimal groups separated by colons. The much larger address space addresses the exhaustion limits of [[IPv4 Address|IPv4]].

Networked games should use address-family-neutral APIs when possible so endpoint handling does not assume one textual format or address size.

IPv6 also reorganizes the packet header and shifts optional functions into extension headers, reducing work for ordinary forwarding. Its larger addresses mean wrappers built only around an IPv4 `sockaddr` layout must be extended rather than treating every endpoint as a 32-bit address plus port.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[multiplayergameprogramming.pdf]]
