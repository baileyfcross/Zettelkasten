2026-10-12 00:45

Status: #baby

Tags: [[Shell Functions and Automation]]

# Shell Here Document

A shell here document supplies a multiline block as standard input to a command until a chosen delimiter line appears. It keeps templates, command input, or explanatory text within the script rather than in a separate file.

Quoting the delimiter controls whether parameter, command, and arithmetic expansion occur inside the block. The `<<-` form can remove leading tab characters for readable indentation, but it does not remove arbitrary spaces.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
