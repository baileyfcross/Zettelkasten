2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Loading]]

# Responsive Image Selection Before Layout

A responsive image candidate may need to be chosen before final layout has computed an exact rendered width. The browser combines viewport information, device pixel density, candidate descriptors, and the author’s `sizes` prediction to make an early choice.

If the markup omits an accurate size estimate, the browser may select an unnecessarily large resource or delay useful work. Responsive markup is therefore a contract that helps loading proceed without waiting for full layout. See [[sizes Attribute]] and [[Responsive Image Candidate Selection]].

# References

[[highperformanceimages.pdf]]
