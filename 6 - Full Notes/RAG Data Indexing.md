2026-09-30 17:53

Status: #baby

Tags: [[Enterprise RAG and Multi-Agent Applications]] [[Microsoft Foundry Data and Model Design]]

# RAG Data Indexing

RAG data indexing extracts governed source material, segments it into searchable units, converts those units to embeddings, and stores them with identifiers and metadata in an index. This prepares enterprise knowledge before any user query arrives.

Index quality depends on document cleaning, chunk boundaries, embedding suitability, authorization metadata, and refresh behavior. Weak preparation cannot be repaired reliably by later generation because relevant evidence may never be retrieved.

In the Foundry example, adding files to a Foundry IQ knowledge source triggers parsing, layout extraction, vectorization, and storage for retrieval. The resulting Ready status is only a pipeline status; representative queries must still confirm that citations resolve to the intended approved documents and that access settings exclude unapproved sources or external browsing.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[microsoftfoundryinaction.pdf]]
