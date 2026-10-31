2026-10-31 13:15

Status: #baby

Tags: [[Java System Runtime Services]]

# Java System Time Methods

`System.currentTimeMillis()` returns the current system time as milliseconds since the Unix epoch at 1970-01-01 00:00:00 UTC. That epoch-relative value can represent a point in time and can be passed to a date representation for human-readable output.

`System.nanoTime()` reads a high-resolution time source whose origin is fixed but arbitrary within one JVM. Its values are therefore suited to measuring elapsed duration by subtracting a start reading from an end reading, not to identifying a calendar date.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
