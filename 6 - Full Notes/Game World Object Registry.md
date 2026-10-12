2026-09-18 17:13

Status: #baby

Tags: [[Game Loop and Object Architecture]]

# Game World Object Registry

A game world object registry stores the objects that participate in particular phases of the [[Game Loop]]. Separate collections can track [[Updateable Game Object|updateable]] and [[Drawable Game Object|drawable]] objects so each phase iterates only applicable instances.

Creation adds an object to the required collections, and removal must take it out of them. Centralizing this membership gives the loop a consistent view of the active world while preserving different object capabilities.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
