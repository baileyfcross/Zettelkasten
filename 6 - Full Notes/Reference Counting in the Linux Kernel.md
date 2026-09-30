2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# Reference Counting in the Linux Kernel

Reference counting records how many active owners keep a kernel object alive, allowing the final release to destroy it when the count reaches zero. Linux provides refcount-oriented operations with stronger misuse checks than treating an ordinary integer as a lifetime counter.

Atomic updates prevent lost increments and decrements, but they do not by themselves make acquiring a reference from an unprotected pointer safe. A separate publication and lookup protocol, often involving a lock or [[Read-Copy-Update]], must ensure the object cannot disappear before the count is increased.

# References

[[linuxkernelprogramming_secondedition.pdf]]
