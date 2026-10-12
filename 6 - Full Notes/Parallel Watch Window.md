2026-09-27 00:11

Status: #baby

Tags: [[.NET Parallel Diagnostics and Testing]]

# Parallel Watch Window

The Parallel Watch window evaluates the same expression across several threads or tasks and displays their values side by side. This helps compare loop indexes, partition state, and shared variables without repeatedly changing the current debugging context.

A watched expression can have different meanings or availability in different stack frames. Evaluation is also a paused observation, so it identifies inconsistent state but does not by itself establish which interleaving produced it.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
