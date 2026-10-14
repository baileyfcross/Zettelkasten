2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# Current Task Pointer

The current task pointer gives kernel code quick access to the [[Linux Task Structure]] of the thread presently running on a CPU. Its implementation is architecture-dependent, but kernel code uses the current macro as a portable abstraction.

Current is meaningful in [[Process Context]], where execution is associated with a schedulable task. In [[Interrupt Context]] it still reflects the task that happened to be interrupted, not an owner that permits the handler to sleep or perform process-context operations.

# References

[[linuxkernelprogramming_secondedition.pdf]]
