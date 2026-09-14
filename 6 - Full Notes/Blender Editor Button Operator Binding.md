2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Editor Button Operator Binding

A core editor can connect a C-created [[Blender UI Button]] to an operation by finding the registered [[Blender Operator Type Structure]] by identifier and assigning that type to the button. The link is established while the header region is drawn.

When the user clicks the button, Blender calls the operation's [[Blender Operator Poll Method]] and then its [[Blender Operator Exec Callback]]. The tutorial's callbacks update the [[Blender Custom SpaceLink Type]] color field and tag the area for redraw, joining interface input to persistent editor state.

# References

[[coreblenderdevelopment.pdf]]

