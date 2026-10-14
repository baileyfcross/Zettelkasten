2026-10-12 00:45

Status: #baby

Tags: [[Unix Text Stream Filters]]

# Sort Text Ordering

The `sort` utility orders input lines and can select keys, delimiters, reverse order, numeric comparison, or version-aware comparison. The selected comparison mode determines whether values such as numbers and dotted version or address components appear in the expected order.

Locale influences collation, so a pipeline that requires reproducible byte or lexical order should set the intended locale. Sorting is also a prerequisite for tools such as `join` and for grouping separated duplicates before [[Uniq Adjacent Duplicate Filtering]].

# References

[[ultimatelinuxshellscriptingguide.pdf]]
