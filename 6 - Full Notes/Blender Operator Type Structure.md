2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Operator Type Structure

`wmOperatorType` is the runtime definition of a Blender operation. It stores a user-facing name and description, a unique identifier, flags, [[Blender Operator RNA Properties]], an optional modal key map, and function pointers for execution, polling, invocation, cancellation, interface, and other behavior.

The type is populated during [[Blender Operator Type Registration]] and found later through the [[Blender Operator Type Registry]]. When a call begins, Blender combines this reusable definition with a new [[Blender Operator Instance Structure]] that carries the operation's current values and transient state.

# References

[[coreblenderdevelopment.pdf]]

