2026-09-28 04:01

Status: #baby

Tags: [[Image Lazy Loading]]

# JavaScript Image Injection and Preloading

When JavaScript assigns an image URL only after execution, the browser’s speculative loader cannot discover that resource from the original markup. The request waits for script download, parsing, execution, and application logic.

That delay is intentional for some lazy-loading designs, but harmful for a hero or product image. Native declarations should carry immediately important resources, while JavaScript control is reserved for requests whose delay is worth the bandwidth savings. See [[Browser Resource Preloader]].

# References

[[highperformanceimages.pdf]]
