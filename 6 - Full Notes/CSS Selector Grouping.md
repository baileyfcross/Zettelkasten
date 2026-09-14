2026-09-14 01:58

Status: #baby

Tags: [[CSS Selectors and Pseudo-Elements]]

# CSS Selector Grouping

Selector grouping assigns the same declaration block to several selectors by separating them with commas. The grouped rule is equivalent to writing a separate rule for each selector, but it keeps shared declarations in one location.

Grouping reduces duplication while preserving independent matching. A malformed selector in a group can invalidate the whole selector list in the CSS generation described by the source, so each member must use valid syntax.

# References

[[css_thedefinitiveguide.pdf]]
