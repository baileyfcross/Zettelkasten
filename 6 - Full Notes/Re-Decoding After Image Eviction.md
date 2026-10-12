2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Decoding and Memory]]

# Re-Decoding After Image Eviction

When a decoded image is evicted from the browser’s memory pool, revisiting it requires reconstructing pixels again from the compressed representation. The repeated CPU work can cause scrolling jank or battery cost even though no new request occurs.

Large images and large sprites consume the pool quickly and increase this risk. Appropriate dimensions and smaller independently useful assets can keep more relevant decoded content resident. See [[Sprite Memory Amplification]].

# References

[[highperformanceimages.pdf]]
