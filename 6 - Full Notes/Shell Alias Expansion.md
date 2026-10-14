2026-10-12 00:45

Status: #baby

Tags: [[Linux Shell Command Environment]]

# Shell Alias Expansion

A shell alias replaces an interactive command word with a predefined text fragment before normal execution. Aliases are useful for convenient default options or short command names, but they are lexical substitutions rather than parameterized reusable program units.

Alias expansion is commonly tied to interactive configuration and may not occur in scripts. A script that needs reusable behavior should use a [[Shell Function]] or an executable command so its dependency is explicit and portable across execution contexts.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
