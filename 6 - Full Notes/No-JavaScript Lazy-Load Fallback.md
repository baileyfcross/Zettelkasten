2026-09-28 04:01

Status: #baby

Tags: [[Image Lazy Loading]]

# No-JavaScript Lazy-Load Fallback

A JavaScript-driven lazy image can fail entirely when scripting is unavailable, blocked, or errors before activation. A fallback should preserve access to meaningful content rather than leaving only a placeholder.

One approach provides a normal image inside `noscript`; another begins with usable markup and progressively enhances behavior where possible. The fallback must also avoid triggering a duplicate eager request in capable clients. Accessibility and content semantics remain important even when the optimization code does not run.

# References

[[highperformanceimages.pdf]]
