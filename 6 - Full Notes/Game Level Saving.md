2026-09-20 23:34

Status: #baby

Tags: [[Game Asset and Level Serialization]]

# Game Level Saving

Game level saving walks the current world and writes global settings followed by each persistent actor, its type, properties, and components. Virtual saving hooks let derived runtime types contribute fields without central code knowing every property.

Transient actors and components may be excluded so temporary effects do not become authored content. The output must conform to the same [[Level File Schema]] expected by [[Game Level Loading]].

# References

[[gameprogrammingincplusplus.pdf]]
