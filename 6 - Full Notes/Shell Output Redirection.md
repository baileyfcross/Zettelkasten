2026-10-12 00:45

Status: #baby

Tags: [[Shell Pipelines and Redirection]]

# Shell Output Redirection

Shell output redirection sends a command's standard output to a file or another descriptor instead of the terminal. The `>` operator replaces the destination file, while `>>` appends new output after its existing contents.

Replacement is destructive and should be used only when the target is intentional. [[Shell Noclobber Option]] can catch some accidental overwrites, but it does not protect files changed by utilities such as `cp`, `mv`, or `rm`.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
