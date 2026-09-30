2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]] [[Linux Kernel Locking]]

# Blocking and Spinning

Blocking suspends a waiting thread so the processor can run other work, but entering and leaving the blocked state requires scheduler and context-switch activity. Spinning keeps checking for progress on the current processor and avoids that transition at the cost of consuming CPU time.

Short waits on a multiprocessor can favor bounded spinning, while long or unpredictable waits favor blocking. A hybrid primitive can spin briefly and then block, matching the cheap path without allowing an extended wait to waste a core.

Linux makes the context distinction mandatory: a [[Mutual Exclusion Lock|kernel mutex]] may sleep and therefore belongs in process context, while a [[SpinLock|kernel spinlock]] must protect only a short nonblocking section and can be used where sleeping is forbidden. Interrupt sharing can additionally require [[Spinlock Interrupt Variants]].

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
