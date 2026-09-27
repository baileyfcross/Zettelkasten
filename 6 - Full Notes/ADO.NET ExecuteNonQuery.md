2026-09-26 22:56

Status: #baby

Tags: [[ADO.NET Database Access]]

# ADO.NET ExecuteNonQuery

`ExecuteNonQuery` runs a command that does not return a row result set, commonly an insert, update, delete, or stored procedure. Its integer result reports the number of rows affected when the provider can supply that information.

The count helps verify the command's effect, such as distinguishing one updated row from an unexpectedly broad update. It is an execution result, not by itself proof that a larger transaction was committed.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

