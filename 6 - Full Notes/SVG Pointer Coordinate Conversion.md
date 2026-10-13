2026-10-12 23:34

Status: #baby

Tags: [[Accessible Interactive and Animated SVG]]

# SVG Pointer Coordinate Conversion

Browser pointer coordinates and SVG user coordinates use different reference frames. `clientX` and `clientY` describe a location in the document viewport, whereas an element may be inside nested viewBox mappings and transforms. Directly copying those values into SVG geometry therefore misplaces points whenever the graphic is scaled or transformed.

`getScreenCTM()` returns the cumulative matrix from an SVG element's local coordinate system to client coordinates. To map a pointer into that local system, create an SVG or DOM point with the event's client coordinates and transform it by the inverse of the element's screen matrix. The result can be used for drawing, dragging, or measuring in the same coordinate system as the target graphic.

This is an application of [[SVG Coordinate Transform Matrices|inverse affine transformation]], not an SVG-specific approximation based on layout width. It remains valid across viewBox scaling, ancestor transforms, and responsive embedding, while ad hoc ratios or historically inconsistent `offsetX` and `offsetY` values do not. Hit selection itself remains the job of [[SVG Pointer Event Hit Testing]].

# References

[[usingsvgwithcss3andhtml5.pdf]]

