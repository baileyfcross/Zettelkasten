2026-10-02 22:40

Status: #baby

Tags: [[Game Network Transport and Serialization]]

# NAT Traversal for Multiplayer Games

NAT traversal for multiplayer games establishes a usable path between hosts whose private addresses are hidden behind network address translation. A router normally creates a mapping after an internal host sends outbound traffic, so an unsolicited packet from another player has no matching entry and is dropped.

Manual port forwarding can create the mapping, while a STUN-style procedure has both players first contact a known public host and then send traffic toward the public address and port observed for the other player. This UDP hole-punching technique depends on the router's mapping behavior and can fail with a symmetric NAT that selects a different external port for each destination. A relay or gamer service can carry traffic when direct traversal is unavailable.

# References

[[multiplayergameprogramming.pdf]]
