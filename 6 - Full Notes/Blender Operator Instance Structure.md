2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Operator Instance Structure

`wmOperator` is the record for one occurrence of an operation. It stores the type identifier, a runtime pointer to the [[Blender Operator Type Structure]], a [[Blender PointerRNA]] containing the current property values, linked-list navigation, and data needed while the operation is being processed.

Because the record is defined in Blender DNA, operator-stack information can be persistent even though callback pointers are resolved at runtime. A [[Blender Non-Modal Operator]] may need it only for one execution, while a [[Blender Modal Operator Lifecycle]] retains instance state across repeated events.

# References

[[coreblenderdevelopment.pdf]]

