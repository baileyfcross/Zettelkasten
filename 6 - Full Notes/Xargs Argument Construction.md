2026-10-12 00:45

Status: #baby

Tags: [[Unix Text Stream Filters]]

# Xargs Argument Construction

The `xargs` utility reads items from standard input and constructs one or more command invocations using those items as arguments. It bridges programs that produce a stream of names with commands that expect an argument list rather than standard input.

Whitespace-delimited parsing is unsafe for arbitrary filenames. When the producer and xargs support it, null-delimited records preserve spaces, quotes, and newlines; batching limits also control command length and the number of items per invocation.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
