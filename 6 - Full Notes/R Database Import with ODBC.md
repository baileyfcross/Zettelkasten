2026-10-04 22:20

Status: #baby

Tags: [[R Data Interchange and External Formats]]

# R Database Import with ODBC

R database import opens a connection to a database, submits a query, and fetches the result into an R object. Database-specific interfaces can connect directly to systems such as MySQL or PostgreSQL, while ODBC provides a common driver-based route to SQL data sources.

The query should select only needed rows and columns when the database is large, and the connection must be closed after use. Credentials and driver configuration belong outside reusable analysis code; the returned object still requires [[R Data Import|import validation]] because database and R types do not always correspond exactly.

# References

[[rprimer.pdf]]
