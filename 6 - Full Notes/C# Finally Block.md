2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Exception Handling]]

# C# Finally Block

A C# `finally` block runs when control leaves its associated `try`, whether the protected work succeeds or throws. It is intended for cleanup that must not depend on which catch block, if any, handles the failure.

Closing a manually managed database connection is a representative use: the resource should be released after both success and failure. Modern disposal constructs often express the same lifetime more directly, but the underlying guarantee remains deterministic cleanup.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

