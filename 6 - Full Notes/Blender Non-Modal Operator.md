2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Non-Modal Operator

A non-modal Blender operator completes its action in one callback rather than remaining active across a sequence of user events. Its type can often be defined with only an [[Blender Operator Exec Callback]] and the [[Blender Operator Poll Method]] that validates the context.

The Outliner select-all example and the custom editor's color buttons follow this form. After [[Blender Operator Handler Dispatch]] locates the registered type, polling checks availability, execution updates data, and the call returns an operator status without entering a [[Blender Modal Operator Lifecycle]].

# References

[[coreblenderdevelopment.pdf]]

