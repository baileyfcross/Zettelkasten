2026-09-30 01:38

Status: #baby

Tags: [[Linux Process and Task Internals]]

# Interrupt Context

Interrupt context is the execution mode entered when the kernel services a hardware interrupt or another asynchronous event. It has no independent process identity, so code in this context cannot rely on the current task as its owner or sleep while waiting for a resource.

Interrupt handlers must remain short and defer extended work to a bottom-half mechanism. Their asynchronous relationship to [[Process Context]] is also why shared data may need interrupt-aware [[Linux Kernel Locking]] rather than an ordinary sleeping lock.

# References

[[linuxkernelprogramming_secondedition.pdf]]
