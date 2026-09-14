2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender SpaceLink Structure

`SpaceLink` is the persistent base layout for an editor instance. It stores linked-list navigation, inactive-region storage, a numeric editor type, flags, and alignment padding; concrete editor records repeat this header before adding their own saved data.

Because it belongs to the [[Blender DNA System]], a space record can be serialized with a blend file. The corresponding runtime behavior lives separately in [[Blender SpaceType Structure]], forming the same data-versus-type pattern used by [[Blender Editor Data-Block Type Pair]].

# References

[[coreblenderdevelopment.pdf]]

