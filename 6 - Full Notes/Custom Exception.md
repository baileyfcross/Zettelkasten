2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Exception Handling]]

# Custom Exception

A custom exception is an application-defined type derived from `Exception` that names a failure not adequately represented by a built-in type. It can provide constructors for a message and an inner exception so callers retain both domain meaning and the original cause.

Creating a custom type is most useful when consumers need to catch that failure distinctly or when the name clarifies a stable application contract. It should not merely rename a standard exception without adding meaning.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

