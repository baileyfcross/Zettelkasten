2026-10-12 00:45

Status: #baby

Tags: [[Bash Variables and Control Flow]]

# Bash Subshell

A Bash subshell is a child shell execution environment created for a grouped command, command substitution, pipeline segment, or explicit parenthesized list. It inherits state from its parent but changes such as directory movement and ordinary variable assignment do not flow back after it exits.

That isolation is useful for temporary context, but it can surprise code that expects a loop or pipeline to update a parent-shell variable. A script should know which constructs execute in the current shell and which establish a child process boundary.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
