2026-09-28 04:01

Status: #baby

Tags: [[Image Lazy Loading]]

# Lazy Loading Preloader Tradeoff

Lazy loading saves bandwidth partly by hiding image URLs from the browser’s early preloader. The same mechanism gives up speculative overlap and may start a needed transfer much later than native markup would.

A good design distinguishes uncertain below-the-fold content from predictable critical content. It does not apply one global lazy behavior merely because the implementation is convenient. The key tradeoff is avoided requests versus lost discovery time.

# References

[[highperformanceimages.pdf]]
