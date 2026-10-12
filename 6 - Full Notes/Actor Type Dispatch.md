2026-09-20 23:34

Status: #baby

Tags: [[Game Asset and Level Serialization]]

# Actor Type Dispatch

Actor type dispatch maps a type name stored in a level file to a function that constructs the corresponding [[Game Actor]] subclass. The loader uses this registry instead of a long conditional chain tied directly to every game type.

The name is persistent data, so changing it can break existing levels. Unknown types should produce a controlled error or fallback rather than a null object that fails later during property loading.

# References

[[gameprogrammingincplusplus.pdf]]
