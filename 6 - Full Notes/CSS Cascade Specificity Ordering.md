2026-09-14 01:58

Status: #baby

Tags: [[CSS Cascade and Inheritance]]

# CSS Cascade Specificity Ordering

After declarations have been grouped by importance and origin, the cascade compares the [[CSS Specificity]] of their selectors. A declaration whose selector has the stronger ordered specificity components wins for the property being resolved.

Specificity cannot move a declaration into a stronger importance or origin group. If two applicable declarations still have equal specificity, [[CSS Source Order Tie-Breaking]] chooses the later one.

# References

[[css_thedefinitiveguide.pdf]]
