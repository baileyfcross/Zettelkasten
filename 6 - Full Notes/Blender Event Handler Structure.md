2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Event Handler Structure

`wmEventHandler` is the common record used to associate event-processing behavior with an editor area or region. It belongs to a linked list, identifies its handler kind, carries flags such as blocking behavior, and can include a poll function that checks whether it applies.

Specialized handlers add information such as key maps or operator callbacks. Editor and region initialization install these records, and the [[Blender Operator Handler Dispatch]] walks them after [[Blender Region Event Routing]] locates the appropriate part of the active screen.

# References

[[coreblenderdevelopment.pdf]]

