2026-10-12 00:45

Status: #baby

Tags: [[Bash Variables and Control Flow]]

# Bash Indexed Array

A Bash indexed array stores multiple values under integer indices within one variable. Array expansion can select one element, all values, all indices, or the number of elements, allowing a loop to preserve item boundaries better than a whitespace-delimited scalar string.

Quoting remains essential when expanding all elements so each stored value becomes one argument. Arrays are a Bash feature rather than a portable POSIX shell facility, which makes them a potential [[Shell Bashism]] in scripts intended for `/bin/sh`.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
