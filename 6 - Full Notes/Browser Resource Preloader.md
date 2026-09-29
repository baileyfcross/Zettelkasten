2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Loading]]

# Browser Resource Preloader

The browser preloader scans ahead for declarative resource references while the main parser may be blocked or busy. It can initiate image, stylesheet, and script fetches without waiting for the full DOM or execution sequence.

Because it acts with incomplete layout knowledge, the preloader uses heuristics and markup hints rather than final visibility. JavaScript-only image URLs are invisible to it until code runs, while native markup gives it an opportunity to overlap work. See [[JavaScript Image Injection and Preloading]].

# References

[[highperformanceimages.pdf]]
