2026-09-14 01:58

Status: #baby

Tags: [[CSS Media Queries and Print Styling]]

# CSS Feature Queries

A CSS feature query uses `@supports` to apply a block only when the user agent supports a tested property-value combination. Browsers that do not understand the at-rule skip the block, making it suitable for optional newer styling.

Tests can be joined with `and`, `or`, and `not`, and feature queries can be nested with [[CSS Media Queries]]. They test declared CSS capability rather than the identity of a browser.

# References

[[css_thedefinitiveguide.pdf]]
