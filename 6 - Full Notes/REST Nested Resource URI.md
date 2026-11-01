2026-10-31 21:16

Status: #baby

Tags: [[REST Resource Contracts and Data Handling]]

# REST Nested Resource URI

A nested resource URI places a related collection or item beneath the identifier of its parent, such as `/posts/{id}/comments`. The hierarchy makes the relationship and the scope of the child request visible in the address.

Nesting is clearest when the child is naturally understood through that parent. The book also cautions against deep paths: long chains become harder to navigate and couple clients to a relationship structure that may later need to change.

# References

[[masteringrestapis.epub]]
