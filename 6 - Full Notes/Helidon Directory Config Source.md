2026-10-19 22:48

Status: #baby

Tags: [[Helidon Configuration System]]

# Helidon Directory Config Source

A Helidon directory config source treats each non-directory file in a selected directory as one configuration entry. The filename becomes the key and the file contents become the corresponding string value.

The example loads separate `username` and `password` files from a secrets directory while disabling environment-variable and system-property sources. This makes the directory an explicit configuration boundary and avoids silently merging values from the process environment.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
