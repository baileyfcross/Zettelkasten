2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender Operator RNA Properties

A Blender operator type points to a [[Blender StructRNA]] that describes the values accepted by that operation. When an operator call begins, Blender creates a [[Blender PointerRNA]] for those properties, sanitizes supplied values, and carries the pointer into the operator instance.

The execution callback reads settings through the [[Blender RNA Access API]] and then passes concrete values to editor and kernel functions. This turns an operator into a bridge between contextual input and the [[Blender DNA RNA Mapping]] that ultimately changes persistent application data.

# References

[[coreblenderdevelopment.pdf]]

