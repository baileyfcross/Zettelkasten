2026-10-12 23:34

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Presentation Attributes and CSS Cascade

An SVG presentation attribute such as `fill`, `stroke`, or `stroke-width` is an XML spelling of a style property. It participates in inheritance, but the cascade treats it as an author declaration with lower priority than any matching stylesheet rule, even a zero-specificity universal selector. A presentation attribute still outranks a value merely inherited from an ancestor.

SVG can also receive styles from inline `style` attributes, internal `style` elements, and external stylesheets. Inline styles outrank ordinary stylesheet rules and presentation attributes, while an `!important` stylesheet declaration can outrank an inline declaration. This hierarchy lets presentation attributes provide robust defaults while classes and stylesheets define themes, media-specific variants, or interactive states.

Presentation attributes lack shorthand forms, duplicate fallback declarations, and `!important`, so conditional fallbacks belong in CSS. With inline [[SVG Embedding Modes|SVG]], the surrounding HTML stylesheet also joins the cascade; that is powerful but means generic selectors can unintentionally cross the HTML-SVG boundary. Structural [[SVG Grouping and Transform Reuse|groups]] can reduce repeated declarations by passing inheritable properties to their children.

# References

[[usingsvgwithcss3andhtml5.pdf]]

