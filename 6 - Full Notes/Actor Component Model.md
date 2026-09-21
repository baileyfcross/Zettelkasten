2026-09-20 23:34

Status: #baby

Tags: [[C++ Game Engine Architecture]]

# Actor Component Model

The actor-component model gives each [[Game Actor]] a small common identity and transform while attaching separate [[Game Component|components]] for capabilities such as movement, drawing, input, audio, or collision. Behavior is composed instead of being forced into a deep inheritance tree.

A hybrid design can still subclass actors for game-specific coordination while reusing components across those subclasses. The model keeps orthogonal features independent and lets one actor own several cooperating behaviors.

# References

[[gameprogrammingincplusplus.pdf]]
