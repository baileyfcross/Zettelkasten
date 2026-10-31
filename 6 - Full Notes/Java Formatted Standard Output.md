2026-10-31 13:15

Status: #baby

Tags: [[Java System Runtime Services]]

# Java Formatted Standard Output

`PrintStream.printf` writes formatted output by combining literal text with format specifiers and a matching sequence of arguments. A specifier begins with `%` and ends with a conversion letter, such as `d` for a decimal integer or `s` for a string.

Width and flag components control alignment, leading spaces, or zero padding, while `%n` emits the platform-appropriate line ending. Each supplied argument must be compatible with the conversion requested by its corresponding specifier.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
