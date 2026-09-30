2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Memory Allocation]]

# Zone Watermarks

Zone watermarks are free-page thresholds that guide Linux memory allocation and reclaim. The minimum level protects reserves needed for forward progress, while low and high thresholds determine when background reclaim starts and when a zone is considered comfortably replenished.

An allocation checks relevant zones against thresholds adjusted for its order and privileges. Falling below the low watermark wakes [[kswapd]], while more severe pressure may force direct [[Kernel Memory Reclaim]] or ultimately contribute to an out-of-memory decision.

# References

[[linuxkernelprogramming_secondedition.pdf]]
