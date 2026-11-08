2026-11-08 14:08

Status: #baby

Tags: [[Jakarta Persistence and Data Access]]

# Jakarta Persistence Embeddable

A Jakarta Persistence embeddable is a value-shaped Java object whose persistent fields are stored as part of an enclosing entity rather than in a table with an independent identity. The value class is marked Embeddable, and an entity includes it through an Embedded field.

The embeddable's fields become columns in the entity's table. This lets related fields such as an address be organized behind a coherent Java type without requiring a separate entity lifecycle or relationship, preserving code readability while using the relational table's ordinary columns.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
