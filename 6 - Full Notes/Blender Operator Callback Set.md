2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Operator Callback Set

A [[Blender Operator Type Structure]] can define callbacks for execution, checking, invocation, cancellation, modal processing, context polling, property polling, interface drawing, dynamic naming, and dynamic descriptions. An operator supplies only the functions required by its interaction model.

A [[Blender Non-Modal Operator]] commonly relies on the [[Blender Operator Exec Callback]] and [[Blender Operator Poll Method]]. A [[Blender Modal Operator Lifecycle]] additionally uses invocation, modal, checking, and cancellation behavior as control passes back and forth between the event system and the operator.

# References

[[coreblenderdevelopment.pdf]]

