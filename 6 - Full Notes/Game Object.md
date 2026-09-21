2026-09-18 17:13

Status: #baby

Tags: [[Game Loop and Object Architecture]]

# Game Object

A game object is a program-level representation of something that participates in the running game world. Different objects may need to update over time, draw visual output, do both, or provide other specialized behavior.

Separating capabilities into interfaces such as [[Updateable Game Object]] and [[Drawable Game Object]] avoids requiring every object to perform every phase. The world can then keep registries organized by behavior rather than by a single rigid class hierarchy.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
