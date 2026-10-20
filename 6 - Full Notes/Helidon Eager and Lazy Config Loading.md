2026-10-19 22:48

Status: #baby

Tags: [[Helidon Configuration System]]

# Helidon Eager and Lazy Config Loading

Helidon config sources can load a complete data set on demand or obtain values one key at a time. `ParsableSource` eagerly supplies an input stream whose format will be parsed, while `NodeConfigSource` eagerly supplies an already constructed object-node tree.

`LazyConfigSource` resolves keys individually. The book identifies eager loading as the preferred source design, while retaining lazy access for stores where loading the complete configuration at once is not the intended behavior.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
