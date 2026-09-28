2026-09-27 21:45

Status: #baby

Tags: [[Azure Network and Resilience Architecture]]

# Azure Double-Hub Architecture

An Azure double-hub architecture separates internet ingress from hybrid connectivity. An ingress hub contains public-facing reverse proxies, web application firewalls, or layer-4 controls, while a hybrid hub connects corporate networks and shared internal services. Online spokes can attach to both paths, whereas corporate spokes attach only to the hybrid hub. The separation clarifies duties and contains policy changes that would otherwise affect every traffic type through one firewall domain.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

