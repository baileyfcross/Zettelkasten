2026-09-09 00:00

Status: #baby

Tags: [[Cloud Security Monitoring and Resilience]] [[Multiplayer Scalability and Security]]

# Man-in-the-Middle Attack

A man-in-the-middle attack places an unauthorized party between communicating endpoints so that it can observe, relay, alter, or substitute information while each endpoint appears to be communicating with the other.

Authenticating endpoints and using an [[Encrypted Communication Channel]] reduce the opportunity for this attack. Integrity checks also help reveal modification, provided their trusted values cannot be replaced by the attacker.

In a networked game, interception can occur on a machine other than the one running the client, allowing packets to be read or modified beyond the reach of local cheat detection. Authentication and encryption are especially important for credentials and other account-sensitive traffic.

An attacker can also alter address-resolution or routing information so each endpoint unknowingly sends traffic through the attacker's host. Public-key cryptography can protect the exchange needed to establish a confidential channel, but a game should reserve its strongest guarantees for passwords, billing data, and other sensitive information rather than assuming every state packet needs the same treatment.

# References

[[cloudcomputing_mit.epub]]
[[gameprogrammingalgorithmsandtechniques.pdf]]

[[multiplayergameprogramming.pdf]]
