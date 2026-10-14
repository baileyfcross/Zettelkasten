2026-10-12 00:45

Status: #baby

Tags: [[Shell Functions and Automation]]

# Shell Function Library

A shell function library is a file of reusable function definitions loaded into the current shell with the dot or `source` command. Sourcing shares functions and other assignments with the caller instead of launching a separate process.

That shared context makes library location and trust important. A script should resolve the intended library rather than depend on an uncontrolled working directory, and the library should avoid performing unrelated actions merely because it was loaded.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
