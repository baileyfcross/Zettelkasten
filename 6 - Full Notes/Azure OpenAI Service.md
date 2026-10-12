2026-09-27 21:45

Status: #baby

Tags: [[Azure AI Application Architecture]]

# Azure OpenAI Service

Azure OpenAI Service provides managed access to generative models through Azure resources, endpoints, deployments, identity, networking, and content-safety controls. An application should separate the model deployment from orchestration, grounding, and business logic so that model versions or routing policies can change without redesigning the entire workload. Capacity, latency, regional availability, token consumption, prompt safety, and monitoring are therefore part of the architecture rather than incidental API details.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
