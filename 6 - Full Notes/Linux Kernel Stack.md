2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# Linux Kernel Stack

Each Linux task has a small, fixed-size kernel stack used while it executes in kernel mode. The stack holds call frames and local automatic variables during system calls, faults, and other kernel paths, while the task's user stack remains part of its user virtual address space.

Because this stack is intentionally limited and cannot expand like a user-space stack, kernel code avoids large local arrays and deep uncontrolled recursion. Interrupt handling may use a separate architecture-specific stack so asynchronous activity does not exhaust the interrupted task's stack.

# References

[[linuxkernelprogramming_secondedition.pdf]]
