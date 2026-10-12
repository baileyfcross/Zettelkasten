2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender Datablock Lifecycle API

Blender's kernel APIs give many datablock types a recognizable lifecycle of initialization, allocation, copying, localization, evaluation, and cleanup. A world or camera interface, for example, exposes operations that create the record in a [[Blender Main Database]] and later release or duplicate its owned data.

Centralizing these behaviors in the [[Blender BKE API]] keeps callers from manipulating persistent layouts ad hoc. The pattern follows [[Blender DNA Kernel Pairing]] by placing state definitions in DNA and application-specific behavior in `blenkernel`.

# References

[[coreblenderdevelopment.pdf]]

