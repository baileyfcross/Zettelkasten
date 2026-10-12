2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# Linux Task Structure

The Linux task structure, represented by task_struct, is the kernel's central descriptor for a schedulable task. It connects identity, credentials, address-space state, open resources, scheduling data, signal handling, and parent-child relationships for both processes and threads.

Linux keeps these structures in linked relationships such as the [[Linux Task List]], while the [[Current Task Pointer]] identifies the descriptor associated with the executing thread. Because task_struct aggregates many subsystems, code normally uses accessors and subsystem APIs instead of modifying its fields casually.

# References

[[linuxkernelprogramming_secondedition.pdf]]
