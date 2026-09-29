2026-09-28 04:01

Status: #baby

Tags: [[Lossless Web Image Formats]]

# GIF Logical Screen and Block Structure

A GIF file is organized as a header followed by a logical screen description and a sequence of typed blocks. Image descriptors identify frame regions, extension blocks carry control or application data, and a trailer marks the end.

This structure permits more than one image and allows metadata-like behavior to be interleaved with frame data. Understanding the block stream explains how animation, palettes, timing, and transparency are assembled rather than treating GIF as a single compressed bitmap. See [[GIF Frame Animation]].

# References

[[highperformanceimages.pdf]]
