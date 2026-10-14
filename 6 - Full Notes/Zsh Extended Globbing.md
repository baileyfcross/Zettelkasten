2026-10-12 00:45

Status: #baby

Tags: [[Alternative Shell and Cross-Platform Scripting]]

# Zsh Extended Globbing

Zsh extended globbing can select filesystem entries by richer patterns and qualifiers, including properties that would otherwise require a separate `find` pipeline. The shell expands the pattern into matching path arguments before the command runs.

Because unmatched patterns and qualifier syntax depend on zsh options, the script should control its option environment and quote data that is not meant to be a glob. Compact selection is valuable only when readers can distinguish patterns from literal filenames.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
