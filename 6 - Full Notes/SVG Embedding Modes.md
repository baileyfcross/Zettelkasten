2026-10-12 23:34

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Embedding Modes

SVG behaves differently depending on how it enters an HTML page. An SVG loaded through `img` or a CSS image value is isolated like a raster image: internal scripts do not run, external resources are not loaded, pointer interaction is disabled, and the host page cannot restyle its internal elements. Declarative animation may still run where supported, while the host supplies alternative text for the image.

An SVG loaded through `object` or `iframe` remains a separate document but may run scripts, load resources, and receive interaction. Communication with the containing page requires document access and is constrained by origin rules. Inline SVG instead joins the HTML document's DOM, so host styles, selectors, scripts, and inherited properties can reach its elements directly.

The choice is architectural rather than cosmetic. Image embedding maximizes encapsulation and cacheable reuse; object embedding preserves document behavior with a boundary; inline markup provides the strongest integration and generally the best access to [[SVG Accessible Names and Descriptions]] and interactive styling. Sizing in every mode still depends on [[SVG Viewport and Canvas]] and the document's intrinsic dimensions.

# References

[[usingsvgwithcss3andhtml5.pdf]]

