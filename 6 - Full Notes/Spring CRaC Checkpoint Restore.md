2026-11-08 16:45

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring CRaC Checkpoint Restore

Spring CRaC integration coordinates a checkpoint of a warmed JVM process and restores that process later, preserving the benefit of JIT-optimized code while avoiding a cold startup path. Managed resources receive callbacks before checkpoint and after restore so connections, files, and other environment-bound state can be released and recreated safely.

CRaC differs from GraalVM Native Image. It restores a JVM snapshot and retains ordinary dynamic Java behavior, while a native image performs closed-world compilation into a standalone executable. Checkpoints may contain sensitive memory and cannot assume that network addresses, credentials, or clocks remain unchanged after restoration.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
