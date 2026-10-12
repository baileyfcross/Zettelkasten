2026-10-12 00:45

Status: #baby

Tags: [[Alternative Shell and Cross-Platform Scripting]]

# Zsh Array Indexing

Zsh array indexing and expansion follow zsh's own defaults, including an index origin and word-expansion behavior that differ from Bash. A direct port of Bash array code can therefore select a different element or produce a different argument list.

Scripts should use zsh-native array syntax consistently and test empty, single-element, and whitespace-containing values. Declaring the intended interpreter is essential when array semantics affect command targets.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
