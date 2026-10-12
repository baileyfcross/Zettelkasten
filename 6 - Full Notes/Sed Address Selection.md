2026-10-12 00:45

Status: #baby

Tags: [[Regular Expressions and Stream Editing]]

# Sed Address Selection

A sed address selects the input records to which an editing command applies. An address can name a line number, the last line, a regular-expression match, or a range between two addresses.

Separating selection from action makes the same substitution, deletion, or insertion precise. Range semantics should be tested on representative data because a start match can activate processing until a later end condition in ways that are not obvious from one sample file.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
