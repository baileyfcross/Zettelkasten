2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# kvmalloc

kvmalloc provides a convenient allocation policy that first attempts [[kmalloc]] and falls back to [[vmalloc]] when physical contiguity is unavailable or impractical. The caller receives a virtually contiguous region without having to duplicate the fallback logic.

Because the underlying allocation kind can vary, callers release it through the matching kvfree interface and must not assume physical contiguity. It is well suited to sizable CPU-only buffers but not to data structures whose hardware interface requires a specific physical layout.

# References

[[linuxkernelprogramming_secondedition.pdf]]
