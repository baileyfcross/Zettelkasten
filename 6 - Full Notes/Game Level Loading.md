2026-09-20 23:34

Status: #baby

Tags: [[Game Asset and Level Serialization]]

# Game Level Loading

Game level loading parses a [[Level File Schema]], applies global properties, constructs actors by type, attaches their components, and assigns saved properties. Construction and property assignment are separate so the correct runtime type exists before specialized values are read.

The loader must handle missing or malformed fields without leaving a partially registered world. Type dispatch and property hooks keep file parsing independent from individual actor classes.

# References

[[gameprogrammingincplusplus.pdf]]
