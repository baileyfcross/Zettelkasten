2026-10-12 00:45

Status: #baby

Tags: [[Shell Pipelines and Redirection]]

# Shell Noclobber Option

The shell `noclobber` option prevents ordinary `>` output redirection from replacing an existing regular file. It acts as an interactive or session-level guard against a common accidental overwrite and can be deliberately overridden when replacement is confirmed.

Noclobber is not a general filesystem safety control. It does not stop appending, deletion, moves, copies, or programs that open files themselves, and a command-line setting disappears when its shell session ends unless startup configuration enables it again.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
