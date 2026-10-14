2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Loading]]

# HTML Image Resource Discovery

An image referenced by an HTML `img` element can be discovered while the browser parses markup. The request can begin before the complete document tree and final layout are available.

Early discovery is valuable because transfer overlaps with parsing and stylesheet work. It also means that later JavaScript or layout cannot always prevent a candidate from being fetched; responsive selection information needs to be present in markup soon enough for the loader. See [[Browser Resource Preloader]] and [[Responsive Image Selection Before Layout]].

# References

[[highperformanceimages.pdf]]
