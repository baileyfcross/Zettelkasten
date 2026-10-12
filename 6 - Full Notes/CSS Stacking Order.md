2026-09-14 01:58

Status: #baby

Tags: [[CSS Floats Positioning and Shapes]]

# CSS Stacking Order

CSS stacking order determines which boxes are painted in front when they overlap. Positioned elements can use `z-index` to establish stack levels, and some values create a new stacking context whose descendants are ordered as a group.

A large descendant `z-index` cannot escape the stacking context of its ancestor to outrank boxes in another higher context. Painting order inside a context also distinguishes backgrounds, in-flow content, floats, and positioned descendants.

# References

[[css_thedefinitiveguide.pdf]]
