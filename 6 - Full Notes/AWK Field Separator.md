2026-10-12 00:45

Status: #baby

Tags: [[AWK Text Processing]]

# AWK Field Separator

The awk field separator defines how an input record is split into fields, while the output field separator defines what `print` places between emitted values. Input separation can be selected at invocation or assigned during program initialization.

Separators are part of the data contract. A simple delimiter works for files such as `/etc/passwd`, but it does not automatically implement CSV quoting or escaping when delimiter characters can occur inside values.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
