2026-09-14 01:58

Status: #baby

Tags: [[CSS Box Model and Normal Flow]]

# CSS Vertical Margin Collapsing

Adjacent vertical margins of qualifying block boxes in normal flow can collapse into one shared margin instead of being added together. The resulting distance generally takes the largest positive margin, with negative margins participating in a combined calculation.

Margins may also collapse between a parent and its first or last in-flow child when no border, padding, or content separates them. Floats, positioned boxes, flex items, and grid items do not follow this ordinary collapsing behavior.

# References

[[css_thedefinitiveguide.pdf]]
