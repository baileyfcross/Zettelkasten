2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Region Event Routing

Region event routing determines which part of the active Blender screen should receive an event. The dispatcher first checks a [[Blender Screen Area Structure]] boundary, then searches its [[Blender Region Structure]] list and sets the matching area and region in context.

This spatial test combines with mode and state checks rather than replacing them. Once the location is known, the event and that region's [[Blender Event Handler Structure]] list pass to [[Blender Operator Handler Dispatch]], where polling can decide whether a candidate operation is valid.

# References

[[coreblenderdevelopment.pdf]]

