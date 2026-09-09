2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ Projection

Projection transforms each input element into a chosen output shape with `Select`. The result may be a single property, a calculated value, an anonymous object, a tuple, or a purpose-built data-transfer type.

Selecting only needed fields separates the consumer's view from the source entity and can reduce data transfer for provider-backed queries. Projection also marks a conceptual boundary: filtering decides which items remain, while projection decides what each remaining item becomes.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
