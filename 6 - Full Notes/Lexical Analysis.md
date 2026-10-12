2026-09-18 17:13

Status: #baby

Tags: [[Game Scripting and Data Formats]]

# Lexical Analysis

Lexical analysis reads a stream of source characters and groups them into tokens such as identifiers, numbers, operators, and keywords. Whitespace and comments are handled according to the language's rules rather than passed directly to later stages.

The token sequence gives [[Syntax Analysis]] a simpler symbolic input. Invalid characters or malformed literals can be reported with source locations during this first stage of a custom scripting language.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
