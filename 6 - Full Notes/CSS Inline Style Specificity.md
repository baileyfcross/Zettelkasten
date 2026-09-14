2026-09-14 01:58

Status: #baby

Tags: [[CSS Cascade and Inheritance]]

# CSS Inline Style Specificity

Declarations in an element's style attribute occupy the inline component of [[CSS Specificity]]. Within declarations of the same importance and origin, this gives [[Inline CSS Styles]] precedence over declarations selected only through IDs, classes, attributes, or element names.

Inline strength does not override every cascade stage. An important declaration can outrank a normal inline declaration because explicit importance is compared before selector specificity.

# References

[[css_thedefinitiveguide.pdf]]
