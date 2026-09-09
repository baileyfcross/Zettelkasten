2026-09-08 21:16

Status: #baby

Tags: [[ASP.NET Core Content Management Systems]]

# CMS Routing

CMS routing maps a public URL, often built from an editor-controlled slug, to a stored content item and the template that renders it. In an ASP.NET Core system this mapping participates in the application's wider routing pipeline.

Slugs should remain unique within their intended scope and stable enough to serve as public identifiers. Changes need redirect or migration policies so editorial reorganization does not silently break incoming links.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
