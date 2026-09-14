2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender RNA Generated Source

During the build, the `makesrna` executable writes `rna_*_gen.c` files into a directory that mirrors the repository's RNA implementation. These generated files contain populated structure and property records, value ranges, enumerations, and backend accessor functions for wrapped DNA types.

The generated code is compiled back into Blender's runtime and works with handwritten repository code. A [[Blender RNA Process Item]] selects each definition function, while the [[Blender RNA Runtime and Generator Phases]] determine which source portions participate in generation and execution.

# References

[[coreblenderdevelopment.pdf]]

