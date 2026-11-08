2026-10-31 21:16

Status: #baby

Tags: [[REST Resource Contracts and Data Handling]]

# REST Resource Model

A REST resource model identifies the domain concepts an API exposes, the properties carried by their representations, and the relationships among them. Operations are then organized around those resources instead of being published as unrelated procedure names.

The book models a blog with collections and individual posts, and a social application with users and their posts. A coherent model gives URI design, validation, serialization, and documentation the same vocabulary, while internal storage can remain a separate implementation decision.

Domain analysis can distinguish independent resources that exist on their own, dependent resources that require another resource, and associative resources that retain their own identity while referring to others. Identifying allowed state transitions then helps determine which HTTP operations the public model needs, before controller code fixes those choices in an implementation.

# References

[[masteringrestapis.epub]]

[[prorestfulapiswithmicronaut.epub]]
