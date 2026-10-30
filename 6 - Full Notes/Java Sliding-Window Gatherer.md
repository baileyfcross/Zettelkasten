2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Sliding-Window Gatherer

The predefined Java `windowSliding(m)` gatherer emits overlapping lists by moving a window of size `m` forward one element at a time. Adjacent results share their last `m-1` values, making local changes across a sequence visible.

It is useful for detecting temperature shifts, market jumps, or other neighborhood patterns. When the entire input is shorter than the requested window, the gatherer emits the available input as one partial window; a custom gatherer is needed for a different step size.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
