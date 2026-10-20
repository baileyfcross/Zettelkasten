2026-10-19 22:48

Status: #baby

Tags: [[Helidon Configuration System]]

# Helidon Config Parser

A Helidon config parser transforms serialized bytes from a configuration source into the in-memory node model. Built-in parsers support Java properties, YAML, JSON, and HOCON when the corresponding configuration artifact is available.

The default lookup chooses the first recognized application file according to priority rather than merging every default-named file. An application can register a custom `ConfigParser` with the builder when its configuration uses another content format.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
