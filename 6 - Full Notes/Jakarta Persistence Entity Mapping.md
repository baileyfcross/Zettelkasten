2026-11-08 14:08

Status: #baby

Tags: [[Jakarta Persistence and Data Access]]

# Jakarta Persistence Entity Mapping

Jakarta Persistence maps a Java class annotated as an Entity to a relational table and maps its instances to rows. The table name defaults from the class, while Table can select a different table and Column can customize a field's column name, nullability, uniqueness, length, precision, or scale.

This mapping keeps the object model expressed in Java while giving the persistence provider enough metadata to generate or use a relational schema. The provider also handles the conversion between compatible Java field types and database column types, so persistence code operates on entity instances rather than manually translating every row.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
