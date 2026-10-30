2026-10-30 15:57

Status: #baby

Tags: [[Java File IO Serialization and Persistence]]

# Java Database Connectivity

JDBC is the Java API for connecting to a relational database, executing SQL, and reading tabular results. A driver creates a `Connection`; statements perform data-definition or data-manipulation work; and a `ResultSet` exposes rows and typed column values.

`PreparedStatement` separates parameter values from SQL text and can be reused safely for repeated shapes, while transactions group operations under explicit commit or rollback. Connections, statements, and result sets are resources that belong in try-with-resources, and production systems usually acquire connections from a managed pool rather than opening one for every operation.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
