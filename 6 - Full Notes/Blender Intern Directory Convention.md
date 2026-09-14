2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Intern Directory Convention

Many Blender modules place implementation source in an `intern/` subdirectory and public interface headers beside it at the module's top level. Functions inside `intern/` may use static linkage for file-local helpers or external linkage for implementation functions that are still not intended as the public API.

The arrangement communicates encapsulation even in C. Callers enter through a [[Blender Module API Boundary]], after which the module can descend into specialized internal work without exposing every helper. The same pattern appears in loaders, kernels, window management, and the [[Blender GHOST Dependency Layer]].

# References

[[coreblenderdevelopment.pdf]]

