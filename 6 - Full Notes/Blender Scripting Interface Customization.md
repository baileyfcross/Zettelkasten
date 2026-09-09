2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Scripting Environment]]

# Blender Scripting Interface Customization

Blender's areas are modular: an area can change editor type, be divided, or be combined with another area. A scripting layout can therefore place a 3D Viewport, Text Editor, Interactive Console, Command Log, and Properties editor together according to the current task.

This configurability turns the interface into part of the development method. Multiple Text Editors help separate a main script from utilities, while a second display can dedicate more room to code or diagnostics. The layout does not create separate data contexts; its editors remain different views onto the same Blender scene.

# References

[[blenderpythonapi.pdf]]
