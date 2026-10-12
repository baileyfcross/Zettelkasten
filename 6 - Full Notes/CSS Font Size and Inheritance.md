2026-09-14 01:58

Status: #baby

Tags: [[CSS Web Typography]]

# CSS Font Size and Inheritance

The `font-size` property accepts absolute-size keywords, relative-size keywords, lengths, and percentages. Relative keywords and percentages are calculated from the inherited font size, while units such as `em` and `rem` refer to element or root font metrics.

Children inherit the computed font size rather than re-running the parent's original percentage expression. This prevents a percentage from compounding at every generation unless it is explicitly declared again.

# References

[[css_thedefinitiveguide.pdf]]
