2026-10-12 23:34

Status: #baby

Tags: [[Accessible Interactive and Animated SVG]]

# SVG Accessible Names and Descriptions

SVG can attach human-readable meaning to the document or to an individual graphical element. A first-child `title` supplies a short name and commonly produces a mouse tooltip; a `desc` supplies a longer explanation. The nearest language declaration should identify the text so assistive technology can pronounce it correctly.

The visible picture determines how much description is needed. A single decorative icon may need only a concise label, while a chart can pair a title with prose describing its important pattern and expose exact values separately in a table. Tooltip text must not be the only carrier of essential information because keyboard and touch users may not be able to reveal it.

Support for native SVG metadata varied substantially in the book's browser era, so `aria-label` or an explicit relationship from `aria-labelledby` to a titled element often made the name more reliable. The name is available only when the chosen [[SVG Embedding Modes|embedding mode]] exposes the SVG document; an HTML `img` normally uses its own alternative text instead. See [[SVG ARIA Roles and Label Relationships]].

# References

[[usingsvgwithcss3andhtml5.pdf]]

