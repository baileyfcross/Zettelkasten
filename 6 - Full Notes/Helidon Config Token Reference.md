2026-10-19 22:48

Status: #baby

Tags: [[Helidon Configuration System]]

# Helidon Config Token Reference

A Helidon config token reference lets one configuration value refer to another key. Tokens begin with a dollar sign and may use braces, as in `$ref` or `${ref}`, while a dotted key such as `${env.ref}` can address a nested value.

Reference resolution reduces repetition across related settings and lets a composed value follow an overridden source value. It is part of the builder's configuration-processing pipeline rather than text substitution performed by the consuming component.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
