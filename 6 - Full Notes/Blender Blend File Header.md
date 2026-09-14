2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender Blend File Header

The blend-file header identifies a valid file with the `BLENDER` signature and records properties required to interpret its bytes. These include the Blender version, pointer size, and whether the writing machine used big- or little-endian byte order.

Both Blender's loader and its repository reader script validate this header before treating the input as a [[Blender Blend File]]. The machine details guide initial decoding, while the [[Blender SDNA Metadata]] supplies the more detailed descriptions used to reconstruct structures.

# References

[[coreblenderdevelopment.pdf]]

