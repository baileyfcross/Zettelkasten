2026-11-08 14:08

Status: #baby

Tags: [[Jakarta Persistence and Data Access]]

# Jakarta Persistence Relationship Mapping

Jakarta Persistence represents associations among entities through one-to-one, many-to-one, one-to-many, and many-to-many mappings. Single-valued relationships hold one associated entity, while collection-valued relationships use a Java collection to represent several associated instances and may require a foreign key or join table in the relational schema.

The mapping states ownership, direction, fetch behavior, and optional cascading of lifecycle operations. A collection of simple or embeddable values is instead an ElementCollection because its members have no independent entity identity. The Java relationship and its relational representation must therefore agree about identity, ownership, and lifecycle.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
