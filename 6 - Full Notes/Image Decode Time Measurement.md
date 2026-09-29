2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Decoding and Memory]]

# Image Decode Time Measurement

Image performance measurement should separate network transfer from the CPU work needed to decode compressed bytes. A resource can be fully downloaded while its pixels are not yet ready to paint.

Decode time can be estimated by forcing or observing image decoding after the data is available and comparing completion timings across formats and dimensions. Measurements should be repeated because scheduling, cache state, and device load introduce noise. See [[Image Decode Throughput]].

# References

[[highperformanceimages.pdf]]
