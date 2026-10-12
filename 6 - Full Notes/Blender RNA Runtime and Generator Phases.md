2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender RNA Runtime and Generator Phases

Blender's RNA build separates non-runtime code that describes and generates an interface from runtime code that executes inside the application. Some repository files contain both portions and use preprocessing to select which part is compiled.

The build first compiles the `makesrna` generator, then emitted files define the runtime macro and include the appropriate source again. This two-phase design lets [[Blender RNA Definition API]] calls produce efficient [[Blender RNA Generated Source]] without requiring every property record and accessor to be written by hand.

# References

[[coreblenderdevelopment.pdf]]

