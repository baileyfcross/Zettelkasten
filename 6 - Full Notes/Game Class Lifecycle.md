2026-09-20 23:34

Status: #baby

Tags: [[C++ Game Engine Architecture]]

# Game Class Lifecycle

A game class lifecycle coordinates initialization, the main [[Game Loop]], and shutdown through one owning object. Initialization creates subsystems and loads data; the loop processes input, updates state, and renders; shutdown releases game data before the libraries it depends on.

Keeping those phases explicit makes partial failure manageable. If initialization stops midway, the game can release only the resources that were successfully created rather than relying on process termination.

# References

[[gameprogrammingincplusplus.pdf]]
