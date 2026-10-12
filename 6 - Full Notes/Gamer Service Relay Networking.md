2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Services and Dedicated Hosting]]

# Gamer Service Relay Networking

Gamer service relay networking sends multiplayer traffic through a platform's identity and transport layer instead of exposing each player's public IP address directly. The service can perform [[NAT Traversal for Multiplayer Games|NAT traversal]], relay packets when a direct route fails, and offer selected reliable or unreliable delivery modes.

The first packet to another user may be delayed while the service establishes a session, so peers can exchange ready messages before starting a synchronized countdown. The abstraction improves reachability and privacy, but the game still owns message semantics, authority, and compatibility with the service's packet limits.

# References

[[multiplayergameprogramming.pdf]]
