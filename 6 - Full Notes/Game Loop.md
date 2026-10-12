2026-09-18 17:13

Status: #baby

Tags: [[Game Loop and Object Architecture]]

# Game Loop

A game loop is the repeating control structure that keeps a game running. Each pass processes input, updates the game world, and generates outputs such as graphics and sound before beginning the next [[Game Frame]].

The order is deliberate: input changes intentions, the update phase advances state, and output presents the resulting state. Timing and object registries turn this simple cycle into a coordinated real-time architecture.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
