2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender Python Method Table

A Python method table maps exposed method names to C function pointers, call flags, and documentation. Blender assigns such an array to an extension type so the interpreter can dispatch a script call to the matching implementation.

Different flags identify instance, class, argument, or no-argument calling conventions. A sentinel entry containing null fields terminates the table. The [[Blender mathutils Vector Method Dispatch]] demonstrates the mapping, while writable attributes can use a separate [[Blender Python Get-Set Definition]].

# References

[[coreblenderdevelopment.pdf]]

