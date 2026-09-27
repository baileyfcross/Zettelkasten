2026-09-06 20:34

Status: #baby

Tags: [[Entity Framework Core Data Modeling]]

# Data Annotation

A data annotation is metadata attached to a model member to express mapping or validation rules. In an Entity Framework Core entity, annotations can identify keys, required values, lengths, or other constraints that cannot be inferred sufficiently from naming conventions alone.

Annotations supplement [[Convention over Configuration]]. They keep simple rules close to the entity definition, while more complicated mapping remains available through explicit model configuration.

In EF Core, attributes can declare mapping details such as keys, required properties, lengths, and relationships close to the entity definition. The book contrasts this convenience with fluent configuration held in the context when mapping concerns should remain external.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
