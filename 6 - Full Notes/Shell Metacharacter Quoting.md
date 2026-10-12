2026-10-12 00:45

Status: #baby

Tags: [[Linux Shell Command Environment]]

# Shell Metacharacter Quoting

Shell metacharacter quoting controls which characters retain syntactic meaning during parsing. Single quotes preserve text literally, double quotes still permit selected expansions, and a backslash escapes one following character according to the surrounding context.

Quoting a variable expansion normally keeps its expanded value as one argument and prevents unintended pathname expansion. A script that omits quotes around filenames or untrusted input can split one value into several words or transform wildcard characters into unrelated paths.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
