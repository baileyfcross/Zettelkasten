2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender RNA Definition API

The RNA definition API consists of `RNA_def_*` functions used to construct the descriptive records for Blender data. Definition code names wrapped structures, associates them with DNA types, describes interface text, creates properties, and installs refine or update callbacks.

Most of this work occurs during the generator phase rather than in the running application. A [[Blender RNA Process Item]] calls the relevant definition function, and the [[Blender makesrna Module]] converts those declarations into [[Blender RNA Generated Source]].

# References

[[coreblenderdevelopment.pdf]]

