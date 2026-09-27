2026-09-26 22:56

Status: #baby

Tags: [[ADO.NET Database Access]]

# ADO.NET DataAdapter

An ADO.NET data adapter bridges a provider's connected commands and a disconnected `DataSet` or `DataTable`. `Fill` loads rows, `FillSchema` loads schema information, and `Update` can transfer supported in-memory changes back to the data source.

The disconnected object does not need to retain connection details while callers inspect or edit its data. The adapter still owns the mapping and command rules required to reconcile those changes with the database.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

