2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# Process Context

Process context is the execution state in which kernel code runs on behalf of a particular user-space task, usually after a system call or exception. The kernel can identify that task through the [[Current Task Pointer]] and can ordinarily sleep because a schedulable process owns the call path.

This context differs from [[Interrupt Context]], which is not attached to a process and must not perform operations that can block. Knowing the current context therefore determines which allocators, locks, and kernel services are safe to use.

# References

[[linuxkernelprogramming_secondedition.pdf]]
