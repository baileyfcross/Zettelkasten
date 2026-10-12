2026-09-26 22:56

Status: #baby

Tags: [[ADO.NET Database Access]]

# ADO.NET ExecuteReader

`ExecuteReader` runs a database command expected to return rows and produces an [[ADO.NET DataReader]]. The caller advances through the forward-only result and retrieves each column by ordinal or name.

This path suits streamed result processing when the application does not need a disconnected, editable in-memory table. The reader and its connection must remain available until consumption finishes.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

