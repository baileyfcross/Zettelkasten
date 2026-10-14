2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Image Width Breakpoint Budget

A width-breakpoint strategy generates a limited series of image dimensions instead of one derivative for every possible viewport. The book proposes adding a new breakpoint when the next larger representation would cost roughly another initial transport window—about 16 packets or 24 KB in its example.

The number is a heuristic, not a universal constant. The useful principle is to space variants by meaningful byte growth so each added derivative saves enough transfer to justify storage, generation, and cache complexity.

# References

[[highperformanceimages.pdf]]
