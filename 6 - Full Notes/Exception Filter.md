2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Exception Handling]]

# Exception Filter

An exception filter adds a `when` condition to a C# catch clause. A handler is selected only when both the exception type and the filter expression match, allowing several handlers for the same type to express different policies.

Filters are useful when an exception carries a stable property that determines whether the current layer can handle it. Matching on fragile message text should be avoided when a typed property or error code is available.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

