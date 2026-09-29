2026-09-15 18:17

Status: #baby

Tags: [[Compositing and Keying]] [[Digital Image Representation and Quality]]

# Alpha Channel as Compositing Matte

An alpha channel is a grayscale description of where an image is visible: white is opaque, black is transparent, and intermediate gray is partially transparent. It can be saved and reused as a selection or mask without changing the source RGB image. In a composite, the matte controls which foreground pixels are mixed with the background. A blurred or feathered alpha gives an edge partial coverage rather than a hard cut, but excessive softness can expose an artificial halo. See [[Feathering a Composite Edge]].

In delivered image formats, alpha is an additional component whose precision determines whether transparency is binary or smoothly graded. That flexibility has a storage and decoded-memory cost, so a format and color type should carry alpha only when the visual needs it. See [[PNG Alpha Transparency]] and [[GIF Binary Transparency]].

# References

[[digitalvisualeffectsandcompositing.pdf]]
[[highperformanceimages.pdf]]
