2026-09-27 21:45

Status: #baby

Tags: [[Azure AI Application Architecture]] [[Microsoft Foundry Data and Model Design]]

# Azure AI Search Vector Store

Azure AI Search can store document fields alongside embedding vectors and retrieve content by semantic similarity. Indexers and enrichment can prepare searchable material, while metadata filters constrain results to an authorized tenant, domain, or time range. A vector index is not merely a database replacement: chunking, embedding-model compatibility, update cadence, access filtering, and retrieval evaluation determine whether the returned context is useful for grounded generation.

Microsoft Foundry can connect an Azure AI Search instance to a project and use its index as the searchable layer behind a knowledge base. This distinguishes indexed reference material from live MCP tools: Search is suited to semantically retrieving prepared content, whereas a tool connection is suited to current records or actions that should not be copied into an index.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

[[microsoftfoundryinaction.pdf]]
