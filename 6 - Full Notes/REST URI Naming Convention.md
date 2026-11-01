2026-10-31 21:16

Status: #baby

Tags: [[REST Resource Contracts and Data Handling]]

# REST URI Naming Convention

A REST URI naming convention gives resources predictable, readable identifiers. The book recommends nouns rather than action verbs, plural names for collections, consistent casing, and shallow hierarchies whose segments express stable resource relationships.

For example, `/users` identifies the collection and `/users/{id}` identifies one user, while the HTTP method carries whether the request retrieves, creates, updates, or deletes. Keeping the operation out of the path separates resource identity from the action applied to it.

# References

[[masteringrestapis.epub]]
