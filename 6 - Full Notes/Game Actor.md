2026-09-20 23:34

Status: #baby

Tags: [[C++ Game Engine Architecture]]

# Game Actor

A game actor is a runtime object with identity, state, transform, and an ordered collection of components. It receives input and update opportunities, then delegates specialized work to its attached [[Game Component|components]].

The actor supplies the shared position, scale, and rotation that rendering, movement, collision, and audio components interpret. Its lifecycle also determines when the world registers or removes the object.

# References

[[gameprogrammingincplusplus.pdf]]
