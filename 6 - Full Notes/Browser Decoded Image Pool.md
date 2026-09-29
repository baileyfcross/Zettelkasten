2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Decoding and Memory]]

# Browser Decoded Image Pool

Browsers keep decoded image surfaces in a bounded memory pool so repeated painting does not require decoding the same compressed resource every time. The pool accelerates display but must yield under device memory pressure.

When the pool fills, the browser evicts decoded surfaces while it may retain the compressed response in cache. Returning to an evicted image avoids the network but requires another decode. See [[Re-Decoding After Image Eviction]].

# References

[[highperformanceimages.pdf]]
