2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# kzalloc

kzalloc has the allocation behavior of [[kmalloc]] but initializes every returned byte to zero. This is useful for structures whose default representation is all-zero and reduces the risk that stale allocator contents are exposed or interpreted as initialized fields.

Zeroing does not replace explicit initialization when zero is not a valid value for every member, nor does it alter lifetime rules. Memory obtained with kzalloc is released with [[kfree]], and the selected [[GFP Flags]] must still match the caller's context.

# References

[[linuxkernelprogramming_secondedition.pdf]]
