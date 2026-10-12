2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender RNA Access API

The RNA access API is the runtime Data API used to read and write properties through [[Blender PointerRNA]] and [[Blender PropertyRNA]] records. Typed functions retrieve or assign scalar and array values without requiring a caller to know the concrete field layout of the wrapped DNA structure.

Its public declarations are separate from the build-time [[Blender RNA Definition API]]. Generated backend functions carry out the actual field access, allowing [[Blender Operator RNA Properties]] and the [[Blender Python RNA Bridge]] to share one descriptive path into Blender state.

# References

[[coreblenderdevelopment.pdf]]

