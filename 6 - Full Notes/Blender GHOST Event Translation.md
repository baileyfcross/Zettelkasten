2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender GHOST Event Translation

Blender's GHOST callback receives portable low-level event types and converts them into application-level work. Window concerns such as opening a file can invoke a registered operator directly, while mouse, key, cursor, and similar input is translated into a Blender event record.

Translation assigns Blender-specific codes, values, coordinates, and custom data before adding the result to a [[Blender Window Event Queue]]. This is the bridge between the [[Blender GHOST Event Consumer]] and the higher [[Blender Event Distribution Pipeline]].

# References

[[coreblenderdevelopment.pdf]]

