2026-10-12 00:45

Status: #baby

Tags: [[Shell Script Security and Reliability]]

# Shell Bashism

A shell Bashism is syntax or behavior provided by Bash but not guaranteed by the POSIX shell language. Double-bracket tests, indexed arrays, certain parameter expansions, and some arithmetic forms are examples that may fail under another `/bin/sh` implementation.

Bashisms are not defects when the script explicitly requires Bash. They become portability defects when the declared interpreter or deployment contract claims broader shell support than the program actually provides.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
