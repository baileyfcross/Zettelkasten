2026-09-06 20:34

Status: #baby

Tags: [[Entity Framework Core Data Modeling]] [[Entity Framework Core Data Access]]

# Code-First Development

Code-first development defines persistent structure through application entity classes and mapping rules, then creates or updates the database from that model. It keeps the data model close to the source code and supports incremental schema evolution.

With [[Entity Framework Core]], a [[Database Context]] assembles the model and an [[Entity Framework Migration]] records the operations needed to bring the database schema into agreement with it.

The web-research project describes EF Core 3 as effectively code-first: application classes and configuration are the continuing source for the database model. An existing database can seed that process through reverse engineering, but later schema evolution proceeds from code.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
