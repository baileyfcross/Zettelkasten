2026-11-08 14:08

Status: #baby

Tags: [[Jakarta Persistence and Data Access]]

# Jakarta Persistence Unit

A Jakarta persistence unit is a logical group of entities that share a data source, transaction type, and persistence settings. Its persistence.xml declaration names the unit and can specify a managed JNDI data source, schema-generation action, entity membership, and other provider properties.

An EntityManager is associated with one persistence unit, so the unit establishes the configuration boundary within which its entities are managed. If entities are not listed explicitly, a Jakarta EE module can bind discovered entities to the unit; the database itself can be located anywhere reachable through the configured data source.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
