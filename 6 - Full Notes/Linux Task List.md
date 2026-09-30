2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# Linux Task List

The Linux task list links the system's [[Linux Task Structure]] instances so the kernel can traverse existing processes and threads. Additional embedded lists and trees represent parent-child, sibling, thread-group, and scheduling relationships without duplicating the task object itself.

Walking task relationships requires the appropriate synchronization or read-copy-update discipline because tasks can exit concurrently. Kernel helpers and iteration macros encode those rules more safely than following raw links without protection.

# References

[[linuxkernelprogramming_secondedition.pdf]]
