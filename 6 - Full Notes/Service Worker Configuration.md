2026-09-06 20:41

Status: #baby

Tags: [[Progressive Web Application Capabilities]]

# Service Worker Configuration

Service worker configuration declares which application resources belong to cache groups and how the worker should retrieve or update them. In Angular, `ngsw-config.json` guides the generated service worker.

Cache rules must match application behavior. A resource used to test live connectivity should not be satisfied from an offline cache, while versioned application assets can be cached to support reliable startup.

# References

[[aspnetcore3andangular9_3ed.pdf]]
