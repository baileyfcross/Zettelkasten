2026-10-12 00:45

Status: #baby

Tags: [[Regular Expressions and Stream Editing]]

# Sed Insert Append and Change

Sed insert, append, and change commands add text before a selected line, add text after it, or replace the selected line or range. Combined with [[Sed Address Selection]], they can restructure a stream without opening the source in an interactive editor.

These commands operate within sed's line-oriented cycle, so their output order differs from a substitution inside the current pattern space. A transformation should first be emitted to a new stream and checked before it replaces an important file.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
