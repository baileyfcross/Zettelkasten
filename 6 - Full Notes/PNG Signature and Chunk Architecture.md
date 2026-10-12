2026-09-28 04:01

Status: #baby

Tags: [[Lossless Web Image Formats]]

# PNG Signature and Chunk Architecture

A PNG begins with a fixed signature that identifies the file and helps detect transfer corruption or incorrect text-mode handling. The rest of the file is a sequence of chunks, each carrying a length, type, data, and integrity check.

This typed-chunk architecture lets decoders recognize essential image information while safely ignoring supported optional information they do not need. Image data may be spread across multiple IDAT chunks, but their payloads form one compressed stream. See [[PNG Critical and Ancillary Chunks]].

# References

[[highperformanceimages.pdf]]
