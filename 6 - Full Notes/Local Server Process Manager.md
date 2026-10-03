2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Services and Dedicated Hosting]]

# Local Server Process Manager

A local server process manager runs on one game-server machine and launches, tracks, and stops its game server processes. It knows the machine's process capacity, assigns identifiers and listening resources, and reports whether the machine is empty, partially used, full, or shutting down.

The manager also monitors child health through exits, heartbeats, or another signal and exposes a control interface to the [[Game Server Virtual Machine Manager]]. Keeping this responsibility local limits the higher-level manager to placement decisions instead of requiring it to supervise every operating-system process directly.

# References

[[multiplayergameprogramming.pdf]]
