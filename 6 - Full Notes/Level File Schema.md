2026-09-20 23:34

Status: #baby

Tags: [[Game Asset and Level Serialization]]

# Level File Schema

A level file schema defines how global settings, actors, components, types, and properties are organized in persistent data. A predictable structure lets the loader validate expected arrays and objects before constructing runtime state.

The schema is a contract between authoring tools and the engine. Adding or renaming fields requires compatibility decisions so older content either receives defaults, migrates, or fails with a useful error.

# References

[[gameprogrammingincplusplus.pdf]]
