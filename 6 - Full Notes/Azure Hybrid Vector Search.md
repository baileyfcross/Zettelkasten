2026-09-27 21:45

Status: #baby

Tags: [[Azure AI Application Architecture]]

# Azure Hybrid Vector Search

Azure hybrid vector search combines vector similarity with lexical search and can add semantic reranking. Vector search captures conceptual resemblance, whereas keyword scoring preserves exact terms, identifiers, and names that embeddings may blur. Combining the result sets generally produces more robust grounding than either method alone. Filters, ranking weights, result count, and evaluation examples should be tuned against the application’s actual questions rather than assumed from a generic benchmark.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
