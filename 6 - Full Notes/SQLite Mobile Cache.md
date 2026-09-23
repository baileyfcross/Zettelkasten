2026-09-22 23:04

Status: #baby

Tags: [[Mobile Data Synchronization and Notifications]]

# SQLite Mobile Cache

A SQLite mobile cache stores structured application data in an embedded relational database on the device. It supports indexed queries and relationships that would be cumbersome in an unstructured key-value cache, while remaining available without a network connection.

Libraries such as SQLite.NET map .NET model attributes to tables and indexes. Local persistence does not itself synchronize with the server; the application must define which records are authoritative and how concurrent changes are resolved.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
