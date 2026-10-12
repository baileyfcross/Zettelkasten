2026-09-28 04:01

Status: #baby

Tags: [[Image Request Consolidation]]

# Data URI Image Inlining

A data URI embeds encoded image bytes directly inside HTML or CSS instead of referencing a separate resource. It removes an image request and makes the bytes available with the containing document.

Inlining increases the parent resource, may add base64 expansion, and prevents the image from having an independent cache lifetime. It is most suitable for small, stable assets used only with that parent. See [[Data URI Cache Tradeoff]].

# References

[[highperformanceimages.pdf]]
