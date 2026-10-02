2026-09-30 17:53

Status: #baby

Tags: [[Enterprise RAG and Multi-Agent Applications]] [[Microsoft Foundry Data and Model Design]]

# Enterprise RAG Data Preparation

Enterprise RAG data preparation converts internal documents into reliable retrieval material by removing obsolete or duplicated content, normalizing structure, preserving headings and metadata, and defining ownership and access rules. The process determines which knowledge the application is allowed to use.

Preparation also establishes update and feedback loops so corrections reach the index rather than remaining in model conversations. Sensitive fields and conflicting versions should be resolved before [[RAG Data Indexing]] to avoid returning unauthorized or ambiguous context.

A Microsoft Foundry knowledge source should therefore contain the latest approved documents, use clear filenames and parseable structure, and exclude drafts or superseded versions. Scanned images without OCR and complex layouts can produce retrieval gaps even when upload succeeds, so indexing status must be followed by test queries that confirm expected passages and citations.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[microsoftfoundryinaction.pdf]]
