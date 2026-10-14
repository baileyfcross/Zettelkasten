2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Loading]]

# DOM Construction and Image Requests

As the HTML parser builds the document object model, it encounters resource-bearing attributes and schedules requests. Parsing can pause for scripts, yet the browser still wants to discover images and styles as early as possible.

Resource discovery and DOM completion are separate milestones. An image request may be in flight before its node participates in final layout, and changing that node later does not undo bytes already requested. The [[Browser Resource Preloader]] exists to keep discovery moving around parser delays.

# References

[[highperformanceimages.pdf]]
