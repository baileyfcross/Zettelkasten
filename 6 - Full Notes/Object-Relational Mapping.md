2026-09-06 20:34

Status: #baby

Tags: [[Entity Framework Core Data Modeling]] [[Entity Framework Core Data Access]]

# Object-Relational Mapping

Object-relational mapping connects an object-oriented application model to tables, columns, keys, and relationships in a relational database. It allows code to create, read, update, and delete persistent data through typed objects instead of writing every data-access operation directly.

[[Entity Framework Core]] performs this mapping from entity classes and a [[Database Context]]. Conventions and [[Data Annotation|annotations]] define how class members correspond to the database model.

The source presents an ORM as a layer that maps application entities and operations to database tables and SQL. This lets code work through domain-shaped objects while the mapper remains responsible for translation, relationships, and persistence commands.

The architecture source explains ORM as a mapping layer between object graphs and relational rows. It reduces repetitive persistence code while leaving query shape, transactions, schema evolution, and provider capabilities as explicit design concerns.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
