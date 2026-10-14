2026-09-27 21:45

Status: #baby

Tags: [[Azure AI Application Architecture]] [[Microsoft Foundry Data and Model Design]]

# Azure Retrieval-Augmented Generation

Azure retrieval-augmented generation retrieves relevant enterprise content at request time and places that context into a generative-model prompt. The pattern lets a model answer from current, organization-specific information without placing all knowledge in model parameters. Its reliability depends on ingestion quality, chunking, retrieval, authorization, prompt construction, citations, and answer evaluation. Retrieval improves grounding, but it does not guarantee that the model will faithfully use the supplied evidence.

In Microsoft Foundry, the pattern can connect source documents, embeddings, and a vector index in Azure AI Search to a user query, retrieved context, model generation, and a cited output. It fits static or semi-static reference material that benefits from synthesis; real-time inventory, prices, or transactional records are often better supplied by an API or MCP tool and combined with the retrieved context.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

[[microsoftfoundryinaction.pdf]]
