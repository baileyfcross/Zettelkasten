2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Decoding and Memory]]

# GPU Image Decoding

Some browsers can use GPU capabilities or GPU-friendly paths to reduce CPU work during image decoding and color conversion. Whether that path is selected remains a browser decision based on format, image properties, and runtime conditions.

Developers can improve eligibility by using supported encodings and sensible dimensions, but should not assume a hint forces hardware decoding. The optimization is valuable when it reduces main-thread pressure and energy use without increasing memory excessively.

# References

[[highperformanceimages.pdf]]
