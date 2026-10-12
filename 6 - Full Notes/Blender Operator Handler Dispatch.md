2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Operator Handler Dispatch

Operator handler dispatch walks the handlers installed for the active area or region and applies them to the current event. Internal handler functions interpret key maps and other handler types, find the relevant [[Blender Operator Type Structure]], poll its context, and call the appropriate callback.

The process is the final stage after [[Blender Region Event Routing]]. Handler status can continue or break propagation, letting one event stop when consumed or move through additional handlers while preserving the context established by the [[Blender Event Distribution Pipeline]].

# References

[[coreblenderdevelopment.pdf]]

