2026-10-12 00:45

Status: #baby

Tags: [[Shell Pipelines and Redirection]]

# Shell File Descriptor

A shell file descriptor is a small integer that identifies an open input or output channel for a process. Descriptors 0, 1, and 2 conventionally represent standard input, standard output, and standard error, while additional descriptors can be opened for other files or streams.

Redirection changes what a descriptor refers to at command launch. Because descriptor duplication is evaluated in order, two superficially similar redirection sequences can send output to different destinations; scripts should express the intended routing explicitly.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
