2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Loading]]

# CSS Background Image Request Discovery

A CSS background image is not discoverable from HTML alone. The browser must fetch and parse the relevant stylesheet, construct enough of the CSS object model, and determine that a rule applies before it knows the URL is needed.

This later discovery can make a visually prominent background start after an equivalent `img`. It can also avoid downloads for rules that never match. The choice between HTML content imagery and CSS decoration therefore affects loading behavior as well as semantics. See [[CSSOM-Dependent Image Loading]].

# References

[[highperformanceimages.pdf]]
