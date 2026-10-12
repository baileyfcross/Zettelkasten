2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Scalability and Security]]

# Client Information Minimization

Client information minimization sends a player only the game state needed to present and control the current experience. Hidden opponents, undiscovered map regions, private inventories, or other secrets cannot be extracted from client memory or packets if the server never transmits them.

The technique complements [[Object Scope and Relevancy]] and server authority. It is particularly valuable against map hacks, while deterministic peer-to-peer games cannot use it fully because every peer may need the complete simulation. Minimization reduces an attacker's information but does not replace transport protection or [[Networked Game Input Validation]].

# References

[[multiplayergameprogramming.pdf]]
