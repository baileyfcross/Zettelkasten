2026-10-12 00:45

Status: #baby

Tags: [[Bash Variables and Control Flow]]

# Shell Command Substitution

Shell command substitution runs a command and replaces the substitution expression with its captured standard output. The `$(...)` form nests more clearly than legacy backticks and can supply a computed value inside an assignment or argument.

Trailing newlines are removed, and an unquoted substitution is subject to word splitting and pathname expansion. The command's output should therefore be treated as data and quoted unless splitting into shell words is intentionally part of the design.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
