2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender RNA Refine Function

An RNA refine function examines a general wrapped DNA record and returns the more specific [[Blender StructRNA]] that describes its runtime subtype. This is useful when several visible types share one underlying C structure but expose different subsets of fields.

Light data illustrates the pattern: a general light record can refine to point, area, spot, or sun descriptions. The function lets [[Blender PointerRNA]] retain one data address while the [[Blender RNA System]] selects the correct properties for access and presentation.

# References

[[coreblenderdevelopment.pdf]]

