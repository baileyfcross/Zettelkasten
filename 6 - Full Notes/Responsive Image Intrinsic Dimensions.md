2026-09-28 04:01

Status: #baby

Tags: [[Responsive Image Selection]]

# Responsive Image Intrinsic Dimensions

Intrinsic dimensions describe an image’s natural width-to-height relationship before CSS layout. When width and height information is available, the browser can reserve the correct aspect ratio before the pixels arrive.

That early geometry reduces layout movement and helps responsive selection reason about the slot. Removing dimension metadata or markup solely to save a few bytes can therefore worsen presentation timing. See [[Lossless JPEG Metadata Optimization]].

# References

[[highperformanceimages.pdf]]
