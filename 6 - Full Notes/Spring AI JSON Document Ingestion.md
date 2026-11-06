2026-10-31 22:16

Status: #baby

Tags: [[Java RAG and Conversational Context]]

# Spring AI JSON Document Ingestion

Spring AI JSON document ingestion uses a JSON reader to select fields from structured records, convert them into `Document` objects, and attach selected metadata before adding the results to a vector store. In the source's product example, descriptive fields form the searchable content while a metadata generator retains identifiers such as the product name and short description.

Structured input does not remove the need for ingestion design. Field selection determines what can be retrieved, metadata determines what can be filtered or traced, and schema changes can invalidate assumptions in later queries. The resulting documents belong to the same [[Spring AI Vector Store Ingestion|controlled vector-ingestion process]] as unstructured material.

# References

[[masteringspringai.epub]]
