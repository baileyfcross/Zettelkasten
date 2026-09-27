2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# Lazy Exception Caching

Lazy initialization may cache an exception thrown by the value factory and rethrow that same failure on later access. Caching makes initialization behave like one attempted operation whose outcome is stable, but it also prevents a transient fault from being retried automatically.

The desired policy depends on whether construction failure is deterministic, recoverable, or affected by external state. Retrying needs an explicit design that avoids uncontrolled duplicate work and makes success after failure visible safely.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
