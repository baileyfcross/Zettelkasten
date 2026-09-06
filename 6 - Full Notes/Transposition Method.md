2026-09-06 00:13

Status: #baby

Tags: [[Search Algorithms]]

# Transposition Method

The transposition method is a [[Self-Organizing Search]] strategy that swaps a found item with the item immediately before it. Each successful access moves the target forward by one position unless it is already first.

Popular items accumulate repeated forward moves and eventually gather near the head, while seldom-used items drift backward. It adapts more slowly than the [[Move-to-Front Algorithm]] but can produce a stronger long-term ordering by access frequency.

# References

[[algorithms.epub]]
