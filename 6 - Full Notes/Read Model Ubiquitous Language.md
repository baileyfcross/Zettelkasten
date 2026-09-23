2026-09-22 20:53

Status: #baby

Tags: [[CQRS Query and Read Model Design]]

# Read Model Ubiquitous Language

Read model Ubiquitous Language names queries and returned information using the terminology of the context and the consumer's decision. Query code does not execute domain behavior, but it remains part of the model because its names express what people ask to know. A generic data-access method hides that intent, whereas an [[Application Query]] such as finding published ads or an owner's listings makes it explicit. The resulting [[Read Model]] should use the same precise vocabulary.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
