2026-10-18 16:30

Status: #baby

Tags: [[Privacy-Preserving Encryption]]

# Search Query Isolation

Search query isolation is the requirement that an encrypted-search server learn as little as possible about a query keyword, stored documents, and the correspondence between keywords and document sets. The source models the server as honest but curious: it performs the required search correctly while still attempting to infer useful information from the protocol.

Encrypted keywords alone are not sufficient if repetitions, access patterns, or index relationships expose the query. [[Searchable Encryption]] therefore has to balance functionality with leakage controls, query authorization, and privacy properties that continue to hold as documents are added or removed.

# References

[[cryptographyandcryptanalysisinjava.epub]]
