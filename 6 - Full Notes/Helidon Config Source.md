2026-10-19 22:48

Status: #baby

Tags: [[Helidon Configuration System]]

# Helidon Config Source

A Helidon config source supplies configuration data to the builder through the `ConfigSource` contract. Built-in sources can read environment variables, Java system properties, classpath resources, files, directories, URLs, strings, maps, and property objects.

The source identifies where data comes from, while a [[Helidon Config Parser]] interprets serialized content and the builder combines resulting nodes. This separation allows the same application configuration model to accept different storage locations and formats.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
