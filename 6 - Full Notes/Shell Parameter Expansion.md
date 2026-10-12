2026-10-12 00:45

Status: #baby

Tags: [[Bash Variables and Control Flow]]

# Shell Parameter Expansion

Shell parameter expansion retrieves a variable or positional parameter and can supply defaults, assign a fallback, report a missing value, calculate length, extract a substring, or remove matching prefixes and suffixes. Curly braces separate the parameter name from surrounding text and hold the selected operator.

Unset and set-but-empty values are not always treated the same; colon variants commonly test both conditions. This distinction lets a script express whether an empty string is valid input or should trigger the same fallback as an absent value.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
