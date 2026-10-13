2026-10-12 23:34

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Use Element Reuse

The SVG `use` element draws a live instance of an element identified elsewhere rather than copying its markup. Definitions are commonly placed in `defs`, while each instance supplies position, transforms, and inherited presentation values. Editing the source definition changes every instance, making `use` the geometry-level counterpart to shared CSS.

The `x` and `y` values translate the instance's coordinate system. `width` and `height` scale reused content only when the source is an `svg` or `symbol` with its own viewBox-like coordinate system; they do not resize an arbitrary shape or group. A `symbol` is never drawn directly and communicates that its contents exist specifically for reuse, which makes it suitable for an [[SVG Symbol Sprite]].

Instances form a shadow-like rendering tree, so event targets and cross-file styles have historically varied between browsers. External reuse also introduces origin restrictions and does not reliably import stylesheet rules from the definition file. Reuse therefore reduces repetition, but the definition should expose intentional inherited styles and remain testable in the chosen [[SVG Embedding Modes|embedding mode]].

# References

[[usingsvgwithcss3andhtml5.pdf]]

