2026-10-12 00:45

Status: #baby

Tags: [[Regular Expressions and Stream Editing]]

# Grep Recursive Search

A grep recursive search walks a directory tree and reports matches from files below it. Include and exclude rules can narrow filenames or directories, while line numbers and filenames preserve the location of each match.

Recursive search should define how to handle binary files, symbolic links, unreadable paths, and generated or vendor directories. Without scope controls, a useful source audit can become slow, noisy, or accidentally inspect sensitive material outside the intended tree.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
