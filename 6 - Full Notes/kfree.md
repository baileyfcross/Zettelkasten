2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# kfree

kfree releases an allocation obtained from [[kmalloc]], [[kzalloc]], or a compatible allocation path back to its slab cache. Passing a null pointer is harmless, but freeing an invalid pointer, freeing twice, or using the object afterward corrupts allocator state and can compromise the kernel.

Correct deallocation requires a clear ownership and lifetime protocol, especially when objects are shared concurrently. [[Reference Counting in the Linux Kernel]] can coordinate the final release, but the counter itself does not make access to the object's contents safe.

# References

[[linuxkernelprogramming_secondedition.pdf]]
