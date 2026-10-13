2026-10-12 23:34

Status: #baby

Tags: [[Accessible Interactive and Animated SVG]]

# SVG Motion Path Animation

Motion-path animation positions an element by distance along a path rather than by independently interpolating x and y. SVG SMIL expresses this with `animateMotion` and an optional `mpath` reference; automatic rotation can align the moving element with the path tangent. Negative start times can stagger repeated instances around a loop.

A scripted equivalent measures the path with `getTotalLength()` and locates a distance with `getPointAtLength()`. Sampling a nearby second point provides a local direction vector, which `atan2` converts into the rotation angle. [[Scripted SVG Animation Frames]] can then update a translate-and-rotate transform from the current timestamp.

The SMIL form is compact and declarative but had incomplete browser support in the source's 2017 context. The JavaScript form is more compatible and controllable but requires explicit interpolation and per-frame DOM updates. Both approaches should leave a meaningful static state and remain subordinate to user control when motion is not essential. See [[SVG SMIL Attribute Animation]].

# References

[[usingsvgwithcss3andhtml5.pdf]]

