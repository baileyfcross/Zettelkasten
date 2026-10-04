2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ Projection

Projection transforms each input element into a chosen output shape with `Select`. The result may be a single property, a calculated value, an anonymous object, a tuple, or a purpose-built data-transfer type.

Selecting only needed fields separates the consumer's view from the source entity and can reduce data transfer for provider-backed queries. Projection also marks a conceptual boundary: filtering decides which items remain, while projection decides what each remaining item becomes.

`SelectMany` extends projection when each input yields a sequence: it flattens those nested results into one output sequence. `Select` preserves one result per input element, so choosing between them determines whether the query retains or removes a level of nesting.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]
