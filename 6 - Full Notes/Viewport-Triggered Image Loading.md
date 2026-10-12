2026-09-28 04:01

Status: #baby

Tags: [[Image Lazy Loading]]

# Viewport-Triggered Image Loading

Viewport-triggered loading requests an image when its element enters or approaches the visible region. A prefetch margin can begin the request early enough that pixels arrive before the user reaches the slot.

A small margin conserves more bandwidth but increases the risk of visible delay during fast scrolling. A large margin behaves more like deferred loading. Tuning therefore depends on network latency, scroll behavior, image weight, and how disruptive a late image would be. See [[Lazy-Load Threshold Tuning]].

# References

[[highperformanceimages.pdf]]
