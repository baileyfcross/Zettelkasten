2026-09-29 23:09

Status: #baby

Tags: [[Blender Character Rigging and Deformation]]

# Driver-Based Facial Rig Controls

Driver-based facial rig controls map a bone transform to the value of one or more facial shape keys. A mouth control might use vertical translation for a smile and scale for opening, allowing the animator to work with visible controls near the face instead of editing many sliders.

The driver specifies the control bone, transform channel, coordinate space, and a curve that converts control motion into the driven value. Local space makes the neutral bone pose a stable reference, while the curve determines direction, sensitivity, and the range over which the expression appears.

# References

[[learningblender3e.pdf]]
