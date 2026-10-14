2026-10-12 00:45

Status: #baby

Tags: [[Shell Pipelines and Redirection]]

# Shell Standard Output

Standard output is file descriptor 1, the conventional stream for a program's primary result. It normally appears in the terminal, but the shell can connect it to a file, a pipeline, or another destination without changing the producing program.

Machine-readable output should contain data rather than progress messages or diagnostics. Keeping that contract allows downstream filters to consume the stream reliably and leaves [[Shell Standard Error]] available for failures and operator-facing context.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
