2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender ContainerRNA

`ContainerRNA` is the common property-container portion embedded in RNA structure descriptions. It maintains linked-list navigation, a property hash, and the ordered list of properties associated with a container.

Within [[Blender StructRNA]], this record gathers the [[Blender PropertyRNA]] objects that describe a wrapped DNA type. Its links also participate in the generated registry of structure descriptions, allowing property lookup to remain organized and efficient at runtime.

# References

[[coreblenderdevelopment.pdf]]

