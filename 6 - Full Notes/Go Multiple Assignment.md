2026-10-19 01:48

Status: #baby

Tags: [[Go Control Flow Functions and Errors]]

# Go Multiple Assignment

Go multiple assignment evaluates a matching list of right-hand expressions and assigns their values to several left-hand destinations. It supports direct swaps, decomposes multiple function results, and separates index-value pairs produced by range iteration.

The positions must be assignment-compatible, and an underscore can intentionally discard a value. Because the right side is evaluated before the assignments take effect, `x, y = y, x` exchanges values without a temporary variable.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
