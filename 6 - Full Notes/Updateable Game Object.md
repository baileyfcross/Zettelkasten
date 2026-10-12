2026-09-18 17:13

Status: #baby

Tags: [[Game Loop and Object Architecture]]

# Updateable Game Object

An updateable game object exposes behavior that advances its state during the update phase of the [[Game Loop]]. Its update operation receives game delta time so movement, animation, and other temporal behavior can remain frame-rate independent.

The [[Game World Object Registry]] can iterate only the objects that require updates. An object that is purely visual or static does not need to implement this capability.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
