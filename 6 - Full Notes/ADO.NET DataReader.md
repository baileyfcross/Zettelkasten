2026-09-26 22:56

Status: #baby

Tags: [[ADO.NET Database Access]]

# ADO.NET DataReader

An ADO.NET data reader provides forward-only access to rows returned by a command. Calling `Read()` advances to the next row, and typed accessors or column indexes retrieve its values.

The reader is efficient for sequential processing because it does not first materialize the entire result into an editable table. It remains connected to the command's data source, so it should be consumed and closed within a clear resource lifetime.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

