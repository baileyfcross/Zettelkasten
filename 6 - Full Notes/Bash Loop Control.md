2026-10-12 00:45

Status: #baby

Tags: [[Bash Variables and Control Flow]]

# Bash Loop Control

Bash loop control uses `while`, `until`, and `for` constructs to repeat commands while a condition holds, until it becomes true, or across a sequence of values. `break` terminates the active loop and `continue` skips the remainder of the current iteration.

Every loop needs an intentional progress condition and correctly quoted iteration values. A forgotten update can produce an infinite loop, while iterating over unquoted command output can silently split records at whitespace instead of preserving the intended items.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
