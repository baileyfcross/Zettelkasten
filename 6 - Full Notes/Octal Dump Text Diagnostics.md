2026-10-12 00:45

Status: #baby

Tags: [[Unix Text Stream Filters]]

# Octal Dump Text Diagnostics

The `od` utility displays the byte-level representation of input in octal, hexadecimal, characters, or other selected formats. It exposes tabs, carriage returns, line feeds, and other invisible bytes that can make a script or configuration file appear correct while parsing incorrectly.

This is especially useful for diagnosing Windows line endings and indentation-sensitive files. The diagnostic view is not a repair by itself; it identifies the exact byte difference that an editor or transformation must remove.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
