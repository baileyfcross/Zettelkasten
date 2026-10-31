2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Ports and Adapters Architecture

Ports and adapters architecture places the application core behind abstract boundaries so user interfaces and infrastructure do not determine its design. Input and output cross ports whose contracts belong with the application, while adapters translate between those contracts and concrete technologies.

The separation lets the same business behavior be driven by a browser, automated test, batch process, or message listener and connected to different databases or external systems. Technology changes are localized in adapters instead of leaking into the reusable core.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

