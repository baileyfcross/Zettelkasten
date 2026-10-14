2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Server-Side Rewind

Server-side rewind evaluates a time-sensitive action against an earlier authoritative world corresponding to what the acting client saw. The server stores recent poses, reads the client's interpolation frame identifiers and fraction, temporarily reconstructs that moment, and performs the hit or interaction test there.

This technique can make an instant-hit weapon feel accurate to the shooter despite latency. It also creates a fairness tradeoff: a target may be judged hit after that player already saw their avatar reach cover. The retained history, maximum rewind window, and eligible actions should therefore be bounded by the game's competitive goals.

# References

[[multiplayergameprogramming.pdf]]
