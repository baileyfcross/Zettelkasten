2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Scalability and Security]]

# Potentially Visible Set

A potentially visible set precomputes which spatial regions might be visible from another region. At runtime, the server locates the client's region and considers objects in its associated set for replication instead of treating the entire world as relevant.

The method suits corridor, room, or track layouts whose visibility structure changes little. A safety margin can include nearby regions to account for movement and network delay. Potential visibility is conservative rather than exact, and gameplay events such as an off-screen explosion can require relevance even when visual tests exclude the source.

# References

[[multiplayergameprogramming.pdf]]
