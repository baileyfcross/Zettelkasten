2026-10-30 15:57

Status: #baby

Tags: [[Java Diagnostics Testing and Documentation]]

# Java Logging Levels

Java logging levels classify records by operational significance so configuration can retain serious events while discarding verbose diagnostics. JUL orders levels from `SEVERE` and `WARNING` through `INFO`, `CONFIG`, `FINE`, `FINER`, and `FINEST`, with `OFF` and `ALL` as bounds.

A logger and its handler can each filter by level, so enabling a detailed logger is insufficient when the destination rejects those records. The selected level should describe the event, not merely make a message visible during development; production configuration can then change volume without editing source.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
