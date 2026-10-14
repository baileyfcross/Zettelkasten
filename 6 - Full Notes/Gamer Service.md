2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Services and Dedicated Hosting]]

# Gamer Service

A gamer service is a platform layer that supplies shared player and game capabilities such as identity, friends, lobbies, matchmaking, networking, statistics, achievements, leaderboards, cloud saves, or platform user interfaces. A game integrates with its asynchronous API and periodically dispatches service callbacks.

Capabilities and account rules differ among services, so game code should depend on an internal abstraction rather than scattering one provider's identifiers and calls through gameplay systems. That boundary makes a later platform port or provider change more manageable while still exposing the features the selected service actually supports.

# References

[[multiplayergameprogramming.pdf]]
