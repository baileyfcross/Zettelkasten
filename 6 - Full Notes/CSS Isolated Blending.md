2026-09-14 01:58

Status: #baby

Tags: [[CSS Filters Blending Clipping and Masking]]

# CSS Isolated Blending

The `isolation` property can force an element to establish a separate stacking context for blending. Descendant blend modes then composite within that group instead of blending directly with content behind the isolated ancestor.

Isolation makes the blend backdrop predictable and prevents a local visual effect from interacting with unrelated page layers. The completed group can still be composited as one result into the surrounding scene.

# References

[[css_thedefinitiveguide.pdf]]
