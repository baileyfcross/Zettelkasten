2026-09-26 22:56

Status: #baby

Tags: [[ADO.NET Database Access]]

# ADO.NET ExecuteScalar

`ExecuteScalar` runs a database command and returns the first column of the first result row as one value. It avoids constructing a row-reading loop when the query asks for a count, aggregate, identifier, or another single result.

The caller must still handle database nulls and convert the returned object to the expected .NET type. A query intended for this method should make the single-value contract explicit.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

