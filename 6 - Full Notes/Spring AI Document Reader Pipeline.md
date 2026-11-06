2026-10-18 23:53

Status: #baby

Tags: [[Java RAG and Conversational Context]]

# Spring AI Document Reader Pipeline

A Spring AI document reader pipeline loads source material into Document objects that carry text and metadata for later transformation, embedding, and storage. Readers adapt file or content formats to the common document representation used by the ingestion process.

Reading is only the first stage of retrieval quality. The pipeline must preserve source identity and useful metadata, choose boundaries that retain meaning, and make ingestion failures visible before vectors are written to a store.

For PDF input, the current source configures a `PagePdfDocumentReader` with page-level extraction, removal of repeated top or bottom lines, and a `TokenTextSplitter` before storage. For structured input, it uses a JSON reader and metadata generator to select content and metadata fields. These two paths share the `Document` boundary while retaining format-specific decisions that affect later retrieval.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
