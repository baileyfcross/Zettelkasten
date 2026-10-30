2026-10-30 15:57

Status: #baby

Tags: [[Java Diagnostics Testing and Documentation]]

# Java Logging Handler and Formatter

In JUL, a handler delivers accepted log records to a destination such as the console or a file. A formatter converts each structured record into text or XML, separating event creation from its storage representation.

Configuration can assign handler-specific levels, file patterns, rotation choices, and formatter classes. A file handler makes persistent postmortem analysis possible, while a console handler is convenient during development. Multiple handlers can receive the same event, but duplicated parent and child handlers can also produce repeated messages if propagation is not configured deliberately.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
