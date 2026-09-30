2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# False Sharing

False sharing occurs when processors modify logically independent variables that occupy the same cache line. The [[Cache Coherence]] protocol must repeatedly transfer or invalidate the entire line, so unrelated updates behave as though they contend for one hardware resource.

Padding, alignment, read-mostly grouping, and [[Per-CPU Variable]] designs can separate hot writers, but they increase memory use and should be guided by measurement. The problem is performance interference rather than a logical data race, so ordinary locking may not remove it.

# References

[[linuxkernelprogramming_secondedition.pdf]]
