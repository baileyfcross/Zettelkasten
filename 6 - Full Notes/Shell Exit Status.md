2026-10-12 00:45

Status: #baby

Tags: [[Bash Variables and Control Flow]]

# Shell Exit Status

A shell exit status is an integer result by which a command reports success or a category of failure to its caller. Zero conventionally means success and nonzero values indicate failure, allowing conditional lists, scripts, and supervising tools to make decisions without parsing display text.

The special parameter `$?` contains the most recently completed command's status and is overwritten by the next command. Scripts should capture or act on it promptly and use documented status values when callers need to distinguish failure modes.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
