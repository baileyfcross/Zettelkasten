2026-10-12 00:45

Status: #baby

Tags: [[Shell Pipelines and Redirection]]

# Shell Standard Input

Standard input is file descriptor 0, the conventional stream from which a process reads data. An interactive command may receive it from the keyboard, while redirection or a pipeline can supply the contents of a file or the output of another process.

Programs designed as filters remain reusable because they do not need to know whether input came from a terminal, file, or pipeline. A script should still distinguish commands that consume standard input from commands that require path arguments.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
