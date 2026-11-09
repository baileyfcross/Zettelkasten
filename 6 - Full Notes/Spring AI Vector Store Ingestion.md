2026-10-18 23:53

Status: #baby

Tags: [[Java RAG and Conversational Context]]

# Spring AI Vector Store Ingestion

Spring AI vector store ingestion prepares documents and adds them to a configured VectorStore, where an embedding model supplies vector representations. The source separates this loading path from the later query path so a corpus can be built before user requests arrive.

A dependable ingestion job records document identity, transformation choices, and embedding configuration. Without those controls, updates can create duplicate chunks or mix incompatible vector spaces, even though each individual write succeeds.

The current source shows both `vectorStore.accept(tokenTextSplitter.apply(pdfReader.get()))` for unstructured PDF pages and `vectorStore.add(documents)` for JSON-derived products. Separating those load endpoints from question answering makes corpus replacement and row-count checks possible without coupling an expensive embedding operation to every user request.

The Spring Boot source configures a PostgreSQL vector store whose embedding dimension must match the selected embedding model. Product knowledge becomes embedded documents that can be retrieved by semantic similarity rather than exact wording. The dimension and embedding provider are therefore schema-level choices: changing them requires a deliberate re-embedding and migration path, not only a model property update.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
