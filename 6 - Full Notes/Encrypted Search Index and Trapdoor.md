2026-10-18 16:30

Status: #baby

Tags: [[Privacy-Preserving Encryption]]

# Encrypted Search Index and Trapdoor

An encrypted search index organizes protected documents by their keywords without requiring the server to store a plaintext lookup structure. The data owner runs a build-index algorithm before uploading the encrypted collection. A data user later derives a trapdoor from an authorized keyword and sends that protected query value to the server.

The server applies the search algorithm to the encrypted index and trapdoor, then returns encrypted matching documents for the user to decrypt. The trapdoor is therefore a capability for one query rather than a disclosure of the raw keyword. Its design and reuse behavior help determine the [[Search Query Isolation]] achieved by [[Searchable Encryption]].

# References

[[cryptographyandcryptanalysisinjava.epub]]
