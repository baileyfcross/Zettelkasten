2026-09-28 21:55

Status: #baby

Tags: [[Blender 3D Viewport and Object Operations]]

# Applying and Clearing Blender Object Transforms

Applying a transform preserves the object's visible result while redefining its current location, rotation, or scale as the new baseline. Clearing a transform instead returns the corresponding values toward their untransformed state.

Unapplied scale can alter how modifiers, constraints, animation, and sculpting interpret dimensions. Applying scale before operations that assume local unit proportions makes their parameters more predictable, but it should be done deliberately because it changes the object's transform history.

The historical Game Engine example applies an actor's rotation and scale before parenting the camera. This makes the actor's present shape the new baseline so the child camera inherits predictable movement rather than carrying unintended residual transform relationships into play.

# References

[[introductiontoblender30.pdf]]

[[testdriveblender.pdf]]
