2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Collections Standard Library and File I-O]]

# Kotlin Collection Transformation

Kotlin's `map` operation applies a transformation function to each source element and returns the resulting values. The result's element type may differ from the source type because the lambda defines a new representation for every input.

Transformations compose with filters and other collection functions to form a pipeline. Each stage states what it contributes—selection, conversion, or aggregation—while the standard library supplies the repetitive traversal and result construction.

# References

[[masteringkotlinforjavadevelopers.epub]]
