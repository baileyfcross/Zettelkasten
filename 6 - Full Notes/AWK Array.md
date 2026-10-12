2026-10-12 00:45

Status: #baby

Tags: [[AWK Text Processing]]

# AWK Array

An awk array associates keys with values and can accumulate counts, group records, or map one representation to another while input is processed. Indices behave as strings, which naturally supports lookup tables as well as numeric-looking keys.

Iteration order is not a reliable substitute for sorted output. When report order matters, keys should be explicitly ordered using supported facilities or emitted into a downstream [[Sort Text Ordering]] stage.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
