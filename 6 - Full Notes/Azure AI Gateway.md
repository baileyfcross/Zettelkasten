2026-09-27 21:45

Status: #baby

Tags: [[Azure AI Application Architecture]]

# Azure AI Gateway

An Azure AI gateway places Azure API Management between AI clients and model endpoints. The gateway can centralize token validation, rate limits, quotas, logging, model routing, load balancing, semantic caching, and policy enforcement while shielding provider-specific endpoints. It creates a stable control plane for multiple applications and models, but gateway policies must account for streamed responses, token-based cost, content sensitivity, latency, and the distinct failure modes of generative services.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
