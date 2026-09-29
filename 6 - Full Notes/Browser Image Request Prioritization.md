2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Loading]]

# Browser Image Request Prioritization

Browsers rank competing requests so critical rendering resources and prominent content can make progress before lower-value images. Initial image priority is often conservative because visibility, position, and dimensions may not yet be known.

Priorities can change after layout reveals which images are in the viewport. Too much parallel work can make every image finish late, so deliberate scheduling may produce useful complete content sooner than unbounded downloading. See [[HTTP2 Stream Priority for Images]].

# References

[[highperformanceimages.pdf]]
