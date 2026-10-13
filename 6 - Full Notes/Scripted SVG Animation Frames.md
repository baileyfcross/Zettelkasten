2026-10-12 23:34

Status: #baby

Tags: [[Accessible Interactive and Animated SVG]]

# Scripted SVG Animation Frames

`requestAnimationFrame()` schedules an update for the browser's next visual refresh instead of demanding a fixed interval. The callback receives a high-resolution timestamp, and a continuing animation requests its next frame from inside the callback. Background tabs are throttled or paused, reducing work that a rapid `setInterval()` loop might continue to demand.

Because frame frequency is not guaranteed, progression should be computed from the timestamp rather than by adding a fixed distance per callback. Interpolation maps elapsed time to a proportion between values; a physics-based loop updates position from velocity, acceleration, and user input. Both approaches remain stable when frames are delayed if time is part of the calculation.

Scripted animation can change attributes, styles, text, DOM order, and element structure, giving it more freedom than [[SVG CSS Transitions and Keyframe Animation]] or [[SVG SMIL Attribute Animation]]. That freedom also moves per-frame computation onto JavaScript and requires explicit stopping, visibility checks, and performance testing. The browser's path-length APIs can support [[SVG Motion Path Animation]] without deriving curve equations manually.

# References

[[usingsvgwithcss3andhtml5.pdf]]

