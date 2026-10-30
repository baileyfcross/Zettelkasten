2026-10-30 15:57

Status: #baby

Tags: [[Java Diagnostics Testing and Documentation]]

# Java Process API

Java's process API can start native operating-system processes and inspect processes visible to the current runtime. `ProcessBuilder` configures a command, environment, directory, and stream redirection, while `Process` exposes input, output, error, completion, and termination operations.

`ProcessHandle` and its information view describe identifiers, ancestry, commands, arguments, start times, and lifecycle without requiring the program to have created the process. Commands and environment syntax remain operating-system-specific, and unread output streams can block a child when their buffers fill.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
