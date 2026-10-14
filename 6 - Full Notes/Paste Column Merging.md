2026-10-12 00:45

Status: #baby

Tags: [[Unix Text Stream Filters]]

# Paste Column Merging

The `paste` utility combines corresponding lines from multiple inputs into one output line, using tabs by default or a selected delimiter. It is a positional merge: first lines align with first lines, second with second, without comparing a key.

This makes paste useful when inputs are already aligned by row. If records must be matched by a shared field rather than position, [[Join Relational Text Merge]] expresses the intended relationship more accurately.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
