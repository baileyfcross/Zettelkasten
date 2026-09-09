2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Architecture]]

# Blender Add-On Distribution

A distributable Blender add-on packages its main initialization file and dependent modules into a predictable directory, commonly delivered as a compressed archive that Blender can install. Metadata describes the package, and registration functions provide the entry points Blender invokes when users enable or disable it.

Distribution should not require recipients to edit development imports or remove diagnostic code. The source's early workflow performs those conversions manually, then its advanced workflow argues for developing directly in the add-on filesystem so the tested structure is already the deployed structure. Packaging is safest when development and installation exercise the same code paths.

# References

[[blenderpythonapi.pdf]]
