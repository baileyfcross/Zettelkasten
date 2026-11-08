2026-11-08 14:08

Status: #baby

Tags: [[Jakarta Persistence and Data Access]]

# Jakarta Persistence Identifier Generation

Every Jakarta Persistence entity needs an identity field marked with Id so the provider can associate the object with a unique database row. GeneratedValue can delegate identifier creation to AUTO or select TABLE, SEQUENCE, or IDENTITY according to the capabilities and portability requirements of the underlying database.

AUTO lets the provider choose an appropriate mechanism, TABLE maintains identifiers through a database table and may allocate blocks in memory, SEQUENCE uses a database sequence where supported, and IDENTITY relies on an auto-number feature during insertion. Choosing a strategy therefore affects portability, schema requirements, and when an identifier becomes available.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
