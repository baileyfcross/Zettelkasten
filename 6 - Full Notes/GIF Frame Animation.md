2026-09-28 04:01

Status: #baby

Tags: [[Lossless Web Image Formats]]

# GIF Frame Animation

An animated GIF places multiple image blocks in one logical screen and uses control extensions to specify frame delay, disposal behavior, and repetition. A frame can cover the whole canvas or update only a smaller region.

Partial updates can save bytes, but the decoder must combine frames according to their disposal rules. Animation therefore emerges from the container’s block sequence rather than from a special moving-image pixel type. See [[GIF Logical Screen and Block Structure]] and [[GIF Binary Transparency]].

# References

[[highperformanceimages.pdf]]
