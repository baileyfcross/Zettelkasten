2026-10-12 00:45

Status: #baby

Tags: [[Bash Variables and Control Flow]]

# Shell Test Expression

A shell test expression evaluates a property of a file, string, or number and reports the result through an exit status. The `test` command and portable single-bracket form require careful token spacing, while Bash's double-bracket form supplies additional pattern and expression behavior.

Tests should quote values according to the selected syntax and compare numbers with numeric operators rather than lexical string operators. The result can drive an `if` statement or a [[Shell Conditional Command List]].

# References

[[ultimatelinuxshellscriptingguide.pdf]]
