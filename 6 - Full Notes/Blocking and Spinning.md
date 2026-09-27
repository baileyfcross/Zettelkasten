2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]]

# Blocking and Spinning

Blocking suspends a waiting thread so the processor can run other work, but entering and leaving the blocked state requires scheduler and context-switch activity. Spinning keeps checking for progress on the current processor and avoids that transition at the cost of consuming CPU time.

Short waits on a multiprocessor can favor bounded spinning, while long or unpredictable waits favor blocking. A hybrid primitive can spin briefly and then block, matching the cheap path without allowing an extended wait to waste a core.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
