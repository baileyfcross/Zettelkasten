2026-10-12 23:34

Status: #baby

Tags: [[Accessible Interactive and Animated SVG]]

# SVG SMIL Attribute Animation

SVG's SMIL-derived animation elements describe time-based changes as document structure. `animate` interpolates an attribute or presentation property, `set` applies a discrete value, `animateTransform` changes a transform, and `animateMotion` moves an element along a path. Timing can be fixed, repeated, chained to other animations, or triggered by a DOM event.

Unlike [[SVG CSS Transitions and Keyframe Animation|CSS animation]], SMIL can target attributes that are not CSS properties and can coordinate multiple independent effects on a shared document timeline. Its base value should still form an acceptable static graphic; a `from` value can create an entrance while leaving the final state in markup for browsers that do not animate.

The source treats support as the decisive limitation: Internet Explorer and Edge did not implement SVG animation elements, while other engines had bugs and uncertain investment. In that browser era, SMIL was best reserved for optional effects, especially where scripts could not run, rather than essential interface behavior. [[SVG Motion Path Animation]] is one of its strongest concise use cases.

# References

[[usingsvgwithcss3andhtml5.pdf]]

