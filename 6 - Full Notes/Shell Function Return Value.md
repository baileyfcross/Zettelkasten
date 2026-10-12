2026-10-12 00:45

Status: #baby

Tags: [[Shell Functions and Automation]]

# Shell Function Return Value

A shell function returns an exit status rather than an arbitrary data object. An explicit `return` sets that status, while omission leaves the status of the last executed command as the function result.

Data can be emitted on standard output and captured with [[Shell Command Substitution]], or assigned through a documented variable interface. Mixing diagnostic messages with returned output makes capture ambiguous, so errors belong on standard error.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
