2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender UI Block

A Blender UI block groups related interface controls within a region. Button-definition functions receive the block so layout, interaction, and selection behavior can be coordinated among controls rather than treating every widget as an isolated drawing command.

The custom editor's header draw callback passes a block while creating each [[Blender UI Button]]. Groups can support relationships such as radial or mutually exclusive choices, and [[Blender Editor Button Operator Binding]] attaches application behavior after the control is defined.

# References

[[coreblenderdevelopment.pdf]]

