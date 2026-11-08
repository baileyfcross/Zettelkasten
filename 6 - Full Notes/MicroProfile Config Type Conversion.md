2026-11-08 14:08

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# MicroProfile Config Type Conversion

MicroProfile Config sources expose raw values as strings, and converters transform those strings into the Java types requested by application code. Built-in converters cover booleans, numeric primitives and wrappers, characters, and classes; the runtime can also derive a converter from a public string constructor or suitable static of, valueOf, or parse method.

A custom Converter supplies parsing and validation for a domain type. Converter priorities resolve competing converters, with the higher priority taking precedence. A reliable converter should be deterministic, thread-safe, explicit about invalid or missing input, and focused solely on the conversion contract.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
