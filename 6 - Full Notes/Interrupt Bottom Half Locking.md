2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Locking]]

# Interrupt Bottom Half Locking

Interrupt bottom-half locking protects data shared with deferred interrupt work such as softirqs and tasklets. Because bottom halves can run asynchronously and may execute on another CPU, code must account for both local preemption by bottom-half processing and true multiprocessor concurrency.

Disabling bottom halves locally prevents same-CPU reentry, while a spinlock serializes cross-CPU access. The combined lock variant encodes both requirements and avoids the self-deadlock that would occur if a bottom half interrupted a process holding its needed lock.

# References

[[linuxkernelprogramming_secondedition.pdf]]
