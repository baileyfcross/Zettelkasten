2026-10-31 22:16

Status: #baby

Tags: [[Java RAG and Conversational Context]]

# Spring AI RAG ETL and Query Separation

Spring AI separates a RAG system into an ingestion path and a request-time query path. The ETL path reads source documents, transforms them into chunks and embeddings, and writes them to a vector store; the query path searches that prepared store, combines selected chunks with the user's question, and asks a chat model to generate the response.

This separation lets [[Spring AI Document Reader Pipeline|document reading]], [[Spring AI Vector Store Ingestion|index construction]], and [[Spring AI Retrieval-Augmented Generation|answer generation]] fail and evolve independently. The two paths must still share compatible embedding models, metadata, authorization rules, and update semantics, while the online path must fit retrieved evidence within a [[RAG Context Window Budget]].

# References

[[masteringspringai.epub]]
