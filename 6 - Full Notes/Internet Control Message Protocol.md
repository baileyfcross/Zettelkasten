2026-09-18 17:13

Status: #baby

Tags: [[Game Network Transport and Serialization]]

# Internet Control Message Protocol

Internet Control Message Protocol carries diagnostic and error information associated with Internet Protocol delivery. Echo request and reply messages support tools that test reachability and estimate round-trip time.

ICMP is not the transport for gameplay state, but its responses can help diagnose connectivity. Firewalls may block or limit messages, so lack of an echo reply does not prove that a game service is unavailable.

The protocol travels as an Internet Protocol payload and communicates network conditions rather than providing application ports. A multiplayer diagnostic can use it to investigate reachability or routing behavior, while the actual game still communicates through TCP or UDP sockets.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[multiplayergameprogramming.pdf]]
