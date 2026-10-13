2026-10-12 23:34

Status: #baby

Tags: [[Accessible Interactive and Animated SVG]]

# SVG CSS Transitions and Keyframe Animation

CSS transitions interpolate a supported property after another state change supplies a new value. Duration, delay, and timing function define how that change unfolds. CSS keyframe animations instead supply named states across an explicit cycle and add controls for repetition, direction, fill behavior, pausing, and timing between keyframes.

For SVG, CSS is concise and can let the browser optimize work or run suitable effects outside the main JavaScript logic. Unsupported transitions degrade to immediate state changes, and unsupported keyframes leave the element's base style, so the unanimated state should remain usable. CSS is especially effective for opacity, color, and other presentation properties.

CSS cannot animate every SVG attribute, and independent animations that write the same property replace rather than automatically add to each other. Long synchronized sequences can also become fragile when expressed as accumulated delays. More attribute-oriented choreography may need [[SVG SMIL Attribute Animation]] or [[Scripted SVG Animation Frames]]. Motion should remain a nonessential enhancement that follows [[Accessible CSS Motion]].

# References

[[usingsvgwithcss3andhtml5.pdf]]

