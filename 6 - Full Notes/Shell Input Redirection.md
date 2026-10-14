2026-10-12 00:45

Status: #baby

Tags: [[Shell Pipelines and Redirection]]

# Shell Input Redirection

Shell input redirection opens a file as a command's standard input, commonly with the `<` operator. The program reads the same stream interface it would use for keyboard or pipeline input, so its processing logic remains independent of the source.

Redirection differs from passing the filename as an argument: in the first case the shell opens the file, while in the second the program decides how to open it. This distinction affects error reporting, support for multiple files, and commands that behave differently when input is a terminal.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
