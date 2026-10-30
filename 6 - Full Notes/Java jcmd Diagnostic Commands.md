2026-10-30 15:57

Status: #baby

Tags: [[Java Diagnostics Testing and Documentation]]

# Java jcmd Diagnostic Commands

`jcmd` sends supported diagnostic commands to a local JVM process. After selecting a PID, it can list available commands and request information or actions involving the heap, class hierarchy, threads, VM flags, native memory, and Java Flight Recorder.

The command set depends on the target JVM and should be inspected with its help output. Some operations, such as heap dumps or forced collection, can be expensive or alter the system being diagnosed; read-only summaries are safer starting points before an intrusive command is used.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
