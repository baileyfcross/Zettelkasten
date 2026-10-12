2026-10-12 00:45

Status: #baby

Tags: [[Regular Expressions and Stream Editing]]

# Sed Program File

A sed program file stores a sequence of editing commands separately from the shell command that supplies input. It makes multi-step substitutions, deletions, insertions, reads, and writes easier to review and reuse than a heavily quoted one-liner.

The program remains sensitive to sed implementation differences, especially around extensions and in-place editing. Keeping source data separate from generated output also provides a safer test and rollback path.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
