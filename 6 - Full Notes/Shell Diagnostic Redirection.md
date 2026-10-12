2026-10-12 00:45

Status: #baby

Tags: [[Shell Pipelines and Redirection]]

# Shell Diagnostic Redirection

Shell diagnostic redirection routes file descriptor 2 independently from ordinary output. A script can save errors to a dedicated file, suppress expected noise, or duplicate standard error onto the current standard-output destination.

Descriptor order matters. Redirecting standard output first and then duplicating standard error onto it combines both streams, whereas duplicating first preserves the destination that standard output had at that earlier moment.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
